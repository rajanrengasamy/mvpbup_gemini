import Papa from 'papaparse';
import type { FinancialData, AggregatedFinancials, Country, ProfitCenter } from '../types/financial';
import { calculateCountryLevelMetrics, aggregateFinancials } from '../utils/financial-calculations';

export async function parseFinancialData(): Promise<Map<string, AggregatedFinancials>> {
  const response = await fetch('/data/q4_2024_financial_data_200k.csv');
  const csvText = await response.text();

  return new Promise((resolve, reject) => {
    Papa.parse<FinancialData>(csvText, {
      header: true,
      dynamicTyping: true,
      skipEmptyLines: true,
      complete: (results) => {
        const countryMetrics = calculateCountryLevelMetrics(results.data);
        resolve(countryMetrics);
      },
      error: (error) => {
        reject(error);
      },
    });
  });
}

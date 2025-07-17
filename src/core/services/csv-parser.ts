import Papa from 'papaparse';
import type { FinancialData, AggregatedFinancials } from '../types/financial';
import { calculateCountryLevelMetrics } from '../utils/financial-calculations';

export async function parseFinancialData(): Promise<Map<string, AggregatedFinancials>> {
  const response = await fetch('/data/q4_2024_financial_data.csv');
  const csvText = await response.text();

  return new Promise((resolve, reject) => {
    Papa.parse<FinancialData>(csvText, {
      header: true,
      dynamicTyping: true,
      skipEmptyLines: true,
      complete: (results: Papa.ParseResult<FinancialData>) => {
        const countryMetrics = calculateCountryLevelMetrics(results.data);
        resolve(countryMetrics);
      },
      error: (error: unknown) => {
        reject(error as Error);
      },
    });
  });
}

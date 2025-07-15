
import type { FinancialData, AggregatedFinancials } from '../types/financial';

export function aggregateFinancials(data: FinancialData[]): AggregatedFinancials {
    return data.reduce((acc, item) => {
        acc.netTradingIncome += item.netTradingIncome;
        acc.otherIncome += item.otherIncome;
        acc.totalIncome += item.totalIncome;
        acc.operatingExpense += item.operatingExpense;
        acc.nonOperatingExpense += item.nonOperatingExpense;
        acc.profitBeforeTax += item.profitBeforeTax;
        acc.tax += item.tax;
        acc.profitAfterTax += item.profitAfterTax;
        acc.capital += item.capital;
        return acc;
    }, {
        netTradingIncome: 0,
        otherIncome: 0,
        totalIncome: 0,
        operatingExpense: 0,
        operatingMargin: 0,
        nonOperatingExpense: 0,
        profitBeforeTax: 0,
        tax: 0,
        profitAfterTax: 0,
        capital: 0,
        returnOnEquity: 0
    });
}

export function calculateCountryLevelMetrics(data: FinancialData[]): Map<string, AggregatedFinancials> {
    const countryData = new Map<string, FinancialData[]>();

    for (const item of data) {
        if (!countryData.has(item.country)) {
            countryData.set(item.country, []);
        }
        countryData.get(item.country)!.push(item);
    }

    const aggregatedData = new Map<string, AggregatedFinancials>();
    for (const [country, countryItems] of countryData.entries()) {
        const aggregated = aggregateFinancials(countryItems);
        aggregated.operatingMargin = aggregated.totalIncome ? (aggregated.totalIncome - aggregated.operatingExpense) / aggregated.totalIncome : 0;
        aggregated.returnOnEquity = aggregated.capital ? aggregated.profitAfterTax / aggregated.capital : 0;
        aggregatedData.set(country, aggregated);
    }

    return aggregatedData;
}

export function calculateProfitCenterMetrics(data: FinancialData[], country: string): Map<string, AggregatedFinancials> {
    const profitCenterData = new Map<string, FinancialData[]>();

    for (const item of data) {
        if (item.country === country) {
            if (!profitCenterData.has(item.profitCenter)) {
                profitCenterData.set(item.profitCenter, []);
            }
            profitCenterData.get(item.profitCenter)!.push(item);
        }
    }

    const aggregatedData = new Map<string, AggregatedFinancials>();
    for (const [pc, pcItems] of profitCenterData.entries()) {
        const aggregated = aggregateFinancials(pcItems);
        aggregated.operatingMargin = aggregated.totalIncome ? (aggregated.totalIncome - aggregated.operatingExpense) / aggregated.totalIncome : 0;
        aggregated.returnOnEquity = aggregated.capital ? aggregated.profitAfterTax / aggregated.capital : 0;
        aggregatedData.set(pc, aggregated);
    }

    return aggregatedData;
}

export function formatCurrency(value: number): string {
    if (Math.abs(value) >= 1e3) {
        return `${(value / 1e3).toFixed(1)}K`;
    }
    return value.toString();
}

export function formatPercentage(value: number): string {
    return `${(value * 100).toFixed(2)}%`;
}

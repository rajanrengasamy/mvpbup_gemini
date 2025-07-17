export interface FinancialMetrics {
  netTradingIncome: number;
  otherIncome: number;
  totalIncome: number;
  operatingExpense: number;
  operatingMargin: number;
  nonOperatingExpense: number;
  profitBeforeTax: number;
  tax: number;
  profitAfterTax: number;
  capital: number;
  returnOnEquity: number;
}

export interface Country extends FinancialMetrics {
  name: string;
  profitCenters: ProfitCenter[];
}

export interface ProfitCenter extends FinancialMetrics {
  name: string;
}

export interface TimeSeriesData {
  [month: string]: AggregatedFinancials;
}

export interface FinancialData {
  date: string;
  country: string;
  profitCenter: string;
  netTradingIncome: number;
  otherIncome: number;
  totalIncome: number;
  operatingExpense: number;
  nonOperatingExpense: number;
  profitBeforeTax: number;
  tax: number;
  profitAfterTax: number;
  capital: number;
}

export type AggregatedFinancials = FinancialMetrics;

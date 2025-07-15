import { writable } from 'svelte/store';
import type { AggregatedFinancials } from '../types/financial';

export const financialData = writable<Map<string, AggregatedFinancials>>(new Map());
export const selectedCountry = writable<string | null>(null);
export const selectedTimePeriod = writable<string>('Monthly');

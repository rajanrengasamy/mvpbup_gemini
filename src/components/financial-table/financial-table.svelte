<script lang="ts">
  import type { AggregatedFinancials } from 'src/core/types/financial';
  import { formatCurrency, formatPercentage } from 'src/core/utils/financial-calculations';

  let { data }: { data: Map<string, AggregatedFinancials> } = $props();

  function calculateTotals() {
    const totals: AggregatedFinancials = {
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
      returnOnEquity: 0,
    };

    for (const value of data.values()) {
      totals.netTradingIncome += value.netTradingIncome;
      totals.otherIncome += value.otherIncome;
      totals.totalIncome += value.totalIncome;
      totals.operatingExpense += value.operatingExpense;
      totals.nonOperatingExpense += value.nonOperatingExpense;
      totals.profitBeforeTax += value.profitBeforeTax;
      totals.tax += value.tax;
      totals.profitAfterTax += value.profitAfterTax;
      totals.capital += value.capital;
    }

    totals.operatingMargin = totals.totalIncome
      ? (totals.totalIncome - totals.operatingExpense) / totals.totalIncome
      : 0;
    totals.returnOnEquity = totals.capital ? totals.profitAfterTax / totals.capital : 0;

    return totals;
  }

  const totals = $derived(calculateTotals());
</script>

<table class="min-w-full border-collapse text-sm">
  <thead class="sticky top-0 bg-blue-900 text-white">
    <tr>
      <th class="px-2 py-1 text-left">Country</th>
      <th class="w-32 px-2 py-1 text-right">Net Trading Income</th>
      <th class="w-32 px-2 py-1 text-right">Other Income</th>
      <th class="w-32 px-2 py-1 text-right">Total Income</th>
      <th class="w-32 px-2 py-1 text-right">Operating Expense</th>
      <th class="w-32 px-2 py-1 text-right">Operating Margin</th>
      <th class="w-32 px-2 py-1 text-right">Non Operating Expense</th>
      <th class="w-32 px-2 py-1 text-right">Profit Before Tax</th>
      <th class="w-32 px-2 py-1 text-right">Tax</th>
      <th class="w-32 px-2 py-1 text-right">Profit After Tax</th>
      <th class="w-32 px-2 py-1 text-right">Capital</th>
      <th class="w-32 px-2 py-1 text-right">Return on Equity</th>
    </tr>
  </thead>
  <tbody>
    {#each Array.from(data.entries()) as [country, metrics], i}
      <tr class={i % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
        <td class="px-2 py-1">{country}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.netTradingIncome)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.otherIncome)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.totalIncome)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.operatingExpense)}</td>
        <td class="px-2 py-1 text-right">{formatPercentage(metrics.operatingMargin)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.nonOperatingExpense)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.profitBeforeTax)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.tax)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.profitAfterTax)}</td>
        <td class="px-2 py-1 text-right">{formatCurrency(metrics.capital)}</td>
        <td class="px-2 py-1 text-right">{formatPercentage(metrics.returnOnEquity)}</td>
      </tr>
    {/each}
    <tr class="font-semibold">
      <td class="px-2 py-1">Grand Total</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.netTradingIncome)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.otherIncome)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.totalIncome)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.operatingExpense)}</td>
      <td class="px-2 py-1 text-right">{formatPercentage(totals.operatingMargin)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.nonOperatingExpense)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.profitBeforeTax)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.tax)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.profitAfterTax)}</td>
      <td class="px-2 py-1 text-right">{formatCurrency(totals.capital)}</td>
      <td class="px-2 py-1 text-right">{formatPercentage(totals.returnOnEquity)}</td>
    </tr>
  </tbody>
</table>

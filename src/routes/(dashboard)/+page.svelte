<script lang="ts">
  import { onMount } from 'svelte';
  import { financialData } from 'src/core/stores/financial.svelte';
  import type { AggregatedFinancials } from 'src/core/types/financial';
  import { parseFinancialData } from 'src/core/services/csv-parser';
  import { FinancialTable } from 'src/components/financial-table';

  let loading = $state(true);

  let dataStore = $state<Map<string, AggregatedFinancials>>(new Map());

  onMount(async () => {
    const data = await parseFinancialData();
    financialData.set(data);
    dataStore = data;
    loading = false;
  });
</script>

<div class="p-4">
  <h1 class="mb-4 text-2xl font-bold">Country Financial Overview</h1>
  {#if loading}
    <p>Loading...</p>
  {:else}
    <div class="overflow-x-auto">
      <FinancialTable data={dataStore} />
    </div>
  {/if}
</div>

<script>
	import Table from './Table.svelte';
	import Settings from './Settings.svelte';
	import Filters from './Filters.svelte';
	import Import from './Import.svelte';
	import History from './History.svelte';
</script>

<div class="flex-1 flex flex-col max-h-full">
	<Settings />
	<Filters />
	<History />
	<Import />
	<Table />
</div>

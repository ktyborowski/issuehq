<script>
	import Drawer from '../../lib/Drawer.svelte';
	import AlphaSlider from './AlphaSlider.svelte';
	import { searchMode, selectedTarget, limit } from '../../stores';

	const targets = [
		{ label: 'Title', value: 'title' },
		{ label: 'Body', value: 'body' },
		{ label: 'All', value: 'body_title' }
	];
</script>

<Drawer id={'search-settings-drawer'} title={'Search settings'}>
	<div class="flex flex-col gap-6">
		<div>
			<label for="limit-select" class="block text-sm font-medium mb-2 dark:text-white">Limit</label>

			<select
				id="limit-select"
				bind:value={$limit}
				class="py-3 px-4 pe-9 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
			>
				<option>25</option>
				<option>50</option>
				<option>100</option>
				<option>250</option>
			</select>
		</div>
		<div>
			<span class="block text-sm font-medium mb-2 dark:text-white">Search in</span>
			<div class="flex flex-col gap-y-3">
				{#each targets as target}
					<div class="flex">
						<input
							type="radio"
							name="hs-radio-vertical-group"
							class="shrink-0 mt-0.5 border-gray-200 rounded-full text-blue-600 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-800 dark:border-neutral-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800"
							id="hs-radio-vertical-group-1"
							bind:group={$selectedTarget}
							value={target.value}
						/>
						<label
							for="hs-radio-vertical-group-1"
							class="text-sm text-gray-500 ms-2 dark:text-neutral-400">{target.label}</label
						>
					</div>
				{/each}
			</div>
		</div>
		{#if $searchMode == 'hybrid'}
			<div class="relative mb-6">
				<label for="input-label" class="block text-sm font-medium mb-2 dark:text-white">Ratio</label
				>
				<AlphaSlider />
				<span class="text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6"
					>Keyword</span
				>
				<span class="text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6"
					>Semantic</span
				>
			</div>
		{/if}
	</div>
</Drawer>

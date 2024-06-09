<script>
	import Drawer from '../../lib/Drawer.svelte';
	import TagInput from './TagInput.svelte';
	import { excludes, selectedState } from '../../stores';

	const states = [
		{ label: 'Open', value: 'open' },
		{ label: 'Closed', value: 'closed' },
		{ label: 'All', value: 'all' }
	];
</script>

<Drawer id={'search-filters-drawer'} title="Search filters">
	<div class="flex flex-col gap-4">
		<div>
			<TagInput list={[]} bind:value={$excludes} />
		</div>
		<div>
			<span class="block text-sm font-medium mb-2 dark:text-white">Status</span>
			<div class="flex flex-col gap-y-3">
				{#each states as state}
					<div class="flex">
						<input
							type="radio"
							name="hs-radio-vertical-group"
							class="shrink-0 mt-0.5 border-gray-200 rounded-full text-blue-600 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-800 dark:border-neutral-700 dark:checked:bg-blue-500 dark:checked:border-blue-500 dark:focus:ring-offset-gray-800"
							id="hs-radio-vertical-group-1"
							bind:group={$selectedState}
							value={state.value}
						/>
						<label
							for="hs-radio-vertical-group-1"
							class="text-sm text-gray-500 ms-2 dark:text-neutral-400">{state.label}</label
						>
					</div>
				{/each}
			</div>
		</div>
	</div>
</Drawer>

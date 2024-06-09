<script>
	import Drawer from '../../lib/Drawer.svelte';
	import {
		searchMode,
		searchQuery,
		searches,
		modeToName,
		fetchIssues,
		selectedTarget,
		alpha,
		excludes,
		selectedState,
		limit
	} from '../../stores';
	import EmptyState from '../../lib/EmptyState.svelte';
	import dayjs from 'dayjs';
	import localizedFormat from 'dayjs/plugin/localizedFormat';
	import pluralize from 'pluralize';

	dayjs.extend(localizedFormat);
</script>

<Drawer id={'search-history-drawer'} title={'Search history'}>
	<!-- End Header -->
	<div class="flex flex-col divide-y">
		{#if $searches}
			{#each $searches as search}
				<div class="py-3 px-4 flex justify-between items-end">
					<div class="">
						<div>
							<p class="font-medium">{search.query}</p>
							<p class="text-sm">
								{search.result_count}
								{pluralize('issue', search.result_count)} found
							</p>
						</div>
						<div class="flex items-center">
							<span class="text-xs">{dayjs(search.created_at).format('LLL')}</span>
							<span class="text-sm">・</span>
							<span
								class="inline-flex items-center gap-x-1.5 py-1 px-2 rounded-full text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-800/30 dark:text-blue-500"
							>
								{modeToName[search.mode]}
							</span>
						</div>
					</div>
					<button
						on:click={() => {
							searchQuery.set(search.query);
							searchMode.set(search.mode);
							fetchIssues(
								search.query,
								search.mode,
								search.limit,
								$selectedTarget,
								$alpha,
								$excludes,
								$selectedState
							);
						}}
						type="button"
						class="py-2 px-3 ml-auto inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							class="flex-shrink-0 size-3.5 text-gray-800 dark:text-neutral-200"
							><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
								d="M19.933 13.041a8 8 0 1 1 -9.925 -8.788c3.899 -1 7.935 1.007 9.425 4.747"
							/><path d="M20 4v5h-5" /></svg
						>
						Rerun
					</button>
				</div>
			{/each}
		{:else}
			<EmptyState
				title={'No previous searches'}
				description={'There are no searches yet. Any search that you make will appear here.'}
			/>
		{/if}
	</div>
</Drawer>

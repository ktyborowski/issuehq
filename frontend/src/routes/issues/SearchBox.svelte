<script>
	import {
		loading,
		searchMode,
		searchModeName,
		searchQuery,
		fetchIssues,
		selectedTarget,
		alpha,
		excludes,
		limit,
		selectedState
	} from '../../stores';
</script>

<div>
	<div>
		<div class="">
			<form class="relative flex rounded-lg shadow-sm">
				<input
					bind:value={$searchQuery}
					type="text"
					id="hs-search-box-with-loading-5"
					name="hs-search-box-with-loading-5"
					class="py-2 px-3 ps-11 block w-full border-gray-200 shadow-sm rounded-s-lg text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
					placeholder=""
				/>
				<div class="absolute inset-y-0 start-0 flex items-center pointer-events-none ps-4">
					<svg
						class="z-20 flex-shrink-0 size-4 text-gray-400 dark:text-neutral-500"
						xmlns="http://www.w3.org/2000/svg"
						width="24"
						height="24"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
					>
						<circle cx="11" cy="11" r="8"></circle>
						<path d="m21 21-4.3-4.3"></path>
					</svg>
				</div>
				<div class="hs-dropdown relative inline-flex">
					<button
						id="hs-dropdown-default"
						type="button"
						class="-ms-px py-2 px-3 inline-flex justify-center items-center gap-2 border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-600 transition-all text-sm dark:bg-neutral-800 dark:hover:bg-neutral-800 dark:border-neutral-700 dark:text-neutral-400 dark:hover:text-white"
					>
						{$searchModeName}
						<svg
							class="hs-dropdown-open:rotate-180 size-4"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"><path d="m6 9 6 6 6-6" /></svg
						>
					</button>
					<div
						class="hs-dropdown-menu transition-[opacity,margin] duration hs-dropdown-open:opacity-100 opacity-0 hidden min-w-60 bg-white shadow-md rounded-lg p-2 mt-2 dark:bg-neutral-800 dark:border dark:border-neutral-700 dark:divide-neutral-700 after:h-4 after:absolute after:-bottom-4 after:start-0 after:w-full before:h-4 before:absolute before:-top-4 before:start-0 before:w-full"
						aria-labelledby="hs-dropdown-default"
					>
						<a
							on:click={() => searchMode.update(() => 'near_text')}
							class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700"
							href="#"
						>
							Semantic
						</a>
						<a
							on:click={() => searchMode.update(() => 'bm25')}
							class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700"
							href="#"
						>
							Keyword
						</a>
						<a
							on:click={() => searchMode.update(() => 'hybrid')}
							class="flex items-center gap-x-3.5 py-2 px-3 rounded-lg text-sm text-gray-800 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700"
							href="#"
						>
							Hybrid
						</a>
					</div>
				</div>

				<button
					on:click={() =>
						fetchIssues(
							$searchQuery,
							$searchMode,
							$limit,
							$selectedTarget,
							$alpha,
							$excludes,
							$selectedState
						)}
					type="submit"
					class="py-2 px-3 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-e-md border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
				>
					{#if $loading}
						<span
							class="animate-spin inline-block size-4 border-[3px] border-current border-t-transparent text-white rounded-full"
							role="status"
							aria-label="loading"
						>
							<span class="sr-only">Loading...</span>
						</span>
					{/if}
					Search
				</button>
			</form>
		</div>
	</div>
</div>

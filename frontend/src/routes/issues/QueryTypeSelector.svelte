<script>
	import { searchMode } from '../../stores';
</script>

<div class="inline-flex rounded-lg shadow-sm">
	<button
		on:click={() => searchMode.update(() => 'semantic')}
		class:bg-white={$searchMode != 'semantic'}
		class:hover:bg-gray-50={$searchMode != 'semantic'}
		class:bg-blue-600={$searchMode == 'semantic'}
		class:text-white={$searchMode == 'semantic'}
		class:hover:bg-blue-700={$searchMode == 'semantic'}
		type="button"
		class="py-2 px-3 inline-flex justify-center items-center gap-2 -ms-px first:rounded-s-lg first:ms-0 last:rounded-e-lg text-sm font-medium focus:z-10 border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
	>
		Semantic
	</button>
	<button
		on:click={() => searchMode.update(() => 'keyword')}
		class:bg-white={$searchMode != 'keyword'}
		class:hover:bg-gray-50={$searchMode != 'keyword'}
		class:bg-blue-600={$searchMode == 'keyword'}
		class:text-white={$searchMode == 'keyword'}
		class:hover:bg-blue-700={$searchMode == 'keyword'}
		type="button"
		class="py-2 px-3 inline-flex justify-center items-center gap-2 -ms-px first:rounded-s-lg first:ms-0 last:rounded-e-lg text-sm font-medium focus:z-10 border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
	>
		Keyword
	</button>
	<button
		on:click={() => searchMode.update(() => 'hybrid')}
		class:bg-white={$searchMode != 'hybrid'}
		class:hover:bg-gray-50={$searchMode != 'hybrid'}
		class:bg-blue-600={$searchMode == 'hybrid'}
		class:text-white={$searchMode == 'hybrid'}
		class:hover:bg-blue-700={$searchMode == 'hybrid'}
		type="button"
		class="py-2 px-3 inline-flex justify-center items-center gap-2 -ms-px first:rounded-s-lg first:ms-0 last:rounded-e-lg text-sm font-medium focus:z-10 border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
	>
		Hybrid
	</button>
</div>

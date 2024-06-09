<script>
	import Drawer from '../../lib/Drawer.svelte';

	let repositoryName = '';
	let submitted = false;

	async function createRepository() {
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ full_name: repositoryName })
		};
		const res = await fetch(`http://localhost:5000/repositories`, requestOptions);

		submitted = true;
	}
</script>

<Drawer id={'import-drawer'} title="Import issues">
	<div class="flex flex-col gap-4">
		<div>
			<label
				for="input-label-with-helper-text"
				class="block text-sm font-medium mb-2 dark:text-white">Repository name</label
			>
			<input
				bind:value={repositoryName}
				type="text"
				id="input-label-with-helper-text"
				class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
				placeholder=""
				aria-describedby="hs-input-helper-text"
			/>
			<p class="mt-2 text-sm text-gray-500 dark:text-neutral-500" id="hs-input-helper-text">
				The name must include the owner eg. weaviate/weaviate.
			</p>
		</div>

		<button
			on:click={() => createRepository()}
			type="button"
			class="py-2 px-3 w-fit inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
		>
			Import
		</button>
		{#if submitted}
			<!-- Toast -->
			<div
				class="bg-white border border-gray-200 rounded-xl shadow-lg dark:bg-neutral-800 dark:border-neutral-700"
				role="alert"
			>
				<div class="flex p-4">
					<div class="flex-shrink-0">
						<svg
							class="flex-shrink-0 size-4 text-teal-500 mt-0.5"
							xmlns="http://www.w3.org/2000/svg"
							width="16"
							height="16"
							fill="currentColor"
							viewBox="0 0 16 16"
						>
							<path
								d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
							></path>
						</svg>
					</div>
					<div class="ms-3">
						<p class="text-sm text-gray-700 dark:text-neutral-400">
							Your import has been scheduled. The issues will become searchable in a few moments.
						</p>
					</div>
				</div>
			</div>
		{/if}
	</div>
</Drawer>

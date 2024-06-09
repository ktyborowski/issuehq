<script>
	export let value = [];
	export let list = [];
	let input = '';

	function pressed(ev) {
		if (ev.type !== 'blur' && ev.key !== ',' && ev.key !== 'Enter') return;

		input = input.replace(',', '');

		if (input === '') return;

		value = [...value, input];
		input = '';
	}

	function del(idx) {
		value.splice(idx, 1);
		value = value;
	}
</script>

<div>
	<label for="exclude" class="block text-sm font-medium mb-2 dark:text-white">Exclude</label>
	<input
		name="exclude"
		class="py-3 px-4 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
		list="tag_suggestion"
		on:blur={pressed}
		on:keyup={pressed}
		bind:value={input}
	/>
	<div class="mt-4 flex flex-wrap gap-2">
		{#each value as t, i}
			<span
				class="inline-flex items-center gap-x-1.5 py-1.5 px-3 rounded-full text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-800/30 dark:text-blue-500"
			>
				{t} <a href="#del" on:click={() => del(i)}>⨉</a>
			</span>
		{/each}
	</div>
	<datalist id="tag_suggestion">
		{#each list as ts}
			<option>{ts}</option>
		{/each}
	</datalist>
</div>

<style>
</style>

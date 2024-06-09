<script>
	import { onMount } from 'svelte';
	import { messages } from '../../../stores';
	import EmptyState from '../../../lib/EmptyState.svelte';
	import Message from './Message.svelte';

	export let issue;

	let message = '';
	let loading = false;

	const initialMessage = {
		role: 'system',
		content: `You are a friendly AI agent who can answer questions about Github issues. You return your responses in the Markdown format. Below is the issue description you must base your responses on. If you can't make a response to the question based on the provided context response with: 'Sorry, I'm not able to answer your question :('\n\n${issue['body']}`
	};

	onMount(() => messages.set([]));

	async function fetchResponse() {
		if (!message) {
			return;
		}
		loading = true;
		if ($messages.length == 0) {
			messages.set([initialMessage]);
		}

		messages.set([...$messages, { role: 'user', content: message }]);
		message = '';
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ messages: $messages })
		};
		const res = await fetch(
			`http://localhost:5000/issues/${issue['public_id']}/chat`,
			requestOptions
		);

		const data = await res.json();

		messages.set([...$messages, data]);

		loading = false;
	}
</script>

<div class="max-h-[40rem] overflow-y-scroll max-w-4xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
	<ul class="space-y-5">
		{#each $messages as message}
			<Message content={message['content']} role={[message['role']]} />
		{:else}
			<EmptyState
				title={'No messages yet'}
				description="Write a message below to start the chat."
			/>
		{/each}
	</ul>
	{#if loading}
		<div class="flex items-center py-4">
			<div
				class="animate-spin inline-block size-6 border-[3px] border-current border-t-transparent text-blue-600 rounded-full dark:text-blue-500"
				role="status"
				aria-label="loading"
			>
				<span class="sr-only">Loading...</span>
			</div>
			<p class="ml-4 text-sm text-gray-600 dark:text-neutral-400">Preparing a response...</p>
		</div>
	{/if}
</div>

<!-- Textarea -->
<footer
	class="max-w-4xl w-full mx-auto sticky bottom-0 z-10 bg-white border-t border-gray-200 pt-2 pb-4 sm:pt-4 sm:pb-6 px-4 sm:px-6"
>
	<div class="flex justify-end items-center mb-3">
		<button
			on:click={() => messages.set([])}
			type="button"
			class="py-1.5 px-2 inline-flex justify-center items-center gap-2 rounded-lg border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 text-xs"
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
				class="flex-shrink-0 size-3"
				><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
					d="M19.95 11a8 8 0 1 0 -.5 4m.5 5v-5h-5"
				/></svg
			>
			Reset
		</button>
	</div>

	<!-- Input -->
	<div class="relative">
		<textarea
			bind:value={message}
			class="p-4 pb-12 block w-full border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none"
			placeholder="Ask anything about the issue..."
		></textarea>

		<!-- Toolbar -->
		<div class="absolute bottom-px inset-x-px p-2 rounded-b-lg bg-white">
			<div class="flex justify-between items-center">
				<!-- Button Group -->
				<div class="flex items-center"></div>
				<!-- End Button Group -->

				<!-- Button Group -->
				<div class="flex items-center gap-x-1">
					<!-- Send Button -->
					<button
						on:click={() => fetchResponse()}
						disabled={loading}
						type="button"
						class="inline-flex flex-shrink-0 justify-center cursor-pointer items-center size-8 rounded-lg text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none"
					>
						<svg
							class="flex-shrink-0 size-3.5"
							xmlns="http://www.w3.org/2000/svg"
							width="16"
							height="16"
							fill="currentColor"
							viewBox="0 0 16 16"
						>
							<path
								d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"
							/>
						</svg>
					</button>
					<!-- End Send Button -->
				</div>
				<!-- End Button Group -->
			</div>
		</div>
		<!-- End Toolbar -->
	</div>
	<!-- End Input -->
</footer>
<!-- End Textarea -->
<!-- End Content -->

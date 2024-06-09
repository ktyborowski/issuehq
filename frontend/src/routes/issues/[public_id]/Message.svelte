<script>
	import DOMPurify from 'dompurify';
	import { marked } from 'marked';

	export let role;
	export let content;
</script>

{#if role == 'assistant'}
	<li class="flex gap-x-2 sm:gap-x-4">
		<span
			class="flex-shrink-0 inline-flex items-center justify-center size-[38px] rounded-full bg-blue-600"
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
				class="text-white"
				><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
					d="M18 4a3 3 0 0 1 3 3v8a3 3 0 0 1 -3 3h-5l-5 3v-3h-2a3 3 0 0 1 -3 -3v-8a3 3 0 0 1 3 -3h12z"
				/><path d="M9.5 9h.01" /><path d="M14.5 9h.01" /><path d="M9.5 13a3.5 3.5 0 0 0 5 0" /></svg
			>
		</span>
		<!-- Card -->
		<div class="bg-white border border-gray-200 rounded-lg p-4 space-y-3">
			<div class="space-y-1.5">
				<p class="mb-1.5 text-sm text-gray-800">
					{@html DOMPurify.sanitize(marked.parse(content))}
				</p>
			</div>
		</div>
		<!-- End Card -->
	</li>
{:else if role == 'user'}
	<li class="max-w-2xl ms-auto flex justify-end gap-x-2 sm:gap-x-4">
		<div class="grow text-end space-y-3">
			<!-- Card -->
			<div class="inline-block bg-blue-600 rounded-lg p-4 shadow-sm">
				<p class="text-sm text-white">{@html DOMPurify.sanitize(marked.parse(content))}</p>
			</div>
			<!-- End Card -->
		</div>

		<span
			class="flex-shrink-0 inline-flex items-center justify-center size-[38px] rounded-full bg-gray-600"
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
				class="text-white"
				><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
					d="M8 7a4 4 0 1 0 8 0a4 4 0 0 0 -8 0"
				/><path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" /></svg
			>
		</span>
	</li>
{/if}

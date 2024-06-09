<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import Chat from './Chat.svelte';
	import Card from '../../../lib/Card.svelte';
	import Clipboard from 'clipboard';
	import EmptyState from '../../../lib/EmptyState.svelte';

	let public_id = $page.params.public_id;
	let copyMessage = '';

	let issue;
	let similarIssues = [];

	async function fetchSimilarIssues() {
		const res = await fetch(`http://localhost:5000/issues/${public_id}/similar`);
		const data = await res.json();

		similarIssues = data;
	}

	onMount(async () => {
		const res = await fetch(`http://localhost:5000/issues/${public_id}`);
		issue = await res.json();

		let clipboard = new Clipboard('#copy-button');
		clipboard.on('success', function (e) {
			e.clearSelection();

			copyMessage = 'Copied!';

			setTimeout(() => (copyMessage = ''), 1000);
		});

		await fetchSimilarIssues();
	});

	let model = 'transformers';

	let loading = false;
	let summary = '';
	async function fetchSummary() {
		summary = '';
		loading = true;

		const searchParams = new URLSearchParams({
			model: model
		});

		const res = await fetch(`http://localhost:5000/issues/${public_id}/summary?` + searchParams);
		const data = await res.json();
		summary = data['content'];
		loading = false;
	}
</script>

{#if issue}
	<div class="grid lg:grid-cols-2 gap-4 flex-1 max-h-full">
		<div class="flex flex-col">
			<div class="page-header">
				<div class="flex flex-col mb-4">
					<div class="-m-1.5 overflow-x-auto">
						<div class="p-1.5 min-w-full inline-block align-middle">
							<div
								class="
          bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden
        "
							>
								<div>
									<div class="px-6 py-4 grid space-y-3">
										<div class="flex justify-between items-center">
											<div>
												<h2 class="text-2xl font-semibold text-gray-800 dark:text-neutral-200">
													{issue.title}
												</h2>
												<div>
													<div
														class="flex items-center gap-2 py-1text-gray-800 decoration-gray-800 dark:text-white dark:decoration-white"
														data-action="click->clipboard#copy"
													>
														<span id="issue-url" class="text-sm">{issue.html_url}</span>
														<button
															id="copy-button"
															data-clipboard-target="#issue-url"
															type="button"
															class="text-sm"
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
																class="icon icon-tabler icons-tabler-outline icon-tabler-copy size-4"
																><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
																	d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"
																/><path
																	d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"
																/></svg
															>
														</button>
														<span class="text-sm">{copyMessage}</span>
													</div>
												</div>

												<div class="flex items-center gap-4 mt-6">
													<div class="inline-flex gap-3">
														<a
															href={issue.html_url}
															target="_blank"
															rel="noopener noreferrer"
															class="flex text-sm items-center gap-1 text-blue-600 hover:text-blue-500 opacity-90"
														>
															View on GitHub
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
																class="size-4"
																><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
																	d="M12 6h-6a2 2 0 0 0 -2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-6"
																/><path d="M11 13l9 -9" /><path d="M15 4h5v5" /></svg
															>
														</a>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- Card -->
			<div class="flex flex-col mb-4">
				<div class="p-1.5 min-w-full inline-block align-middle">
					<div
						class="
          bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden
        "
					>
						<div
							class="
            px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b
            border-gray-200 dark:border-neutral-700
          "
						>
							<div>
								<h2 class="font-semibold text-gray-800 dark:text-neutral-200">Details</h2>
							</div>

							<div>
								<div class="inline-flex gap-x-2"></div>
							</div>
						</div>
						<div>
							<div class="px-6 py-4 grid space-y-3">
								<dl class="grid sm:flex gap-x-3 text-sm">
									<dt class="min-w-36 max-w-[200px] text-gray-500 dark:text-neutral-500">Title</dt>
									<dd class="font-medium text-gray-800 dark:text-neutral-200">
										{issue.title}
									</dd>
								</dl>
								<dl class="grid sm:flex gap-x-3 text-sm">
									<dt class="min-w-36 max-w-[200px] text-gray-500 dark:text-neutral-500">Number</dt>
									<dd class="font-medium text-gray-800 font-mono dark:text-neutral-200">
										#{issue.number}
									</dd>
								</dl>
								<dl class="grid sm:flex gap-x-3 text-sm">
									<dt class="min-w-36 max-w-[200px] text-gray-500 dark:text-neutral-500">Status</dt>
									<dd class="font-medium text-gray-800 dark:text-neutral-200">
										<span
											class="py-1 px-1.5 inline-flex items-center gap-x-1 text-xs font-medium bg-teal-100 text-teal-800 rounded-full"
										>
											<svg
												class="size-2.5"
												xmlns="http://www.w3.org/2000/svg"
												width="16"
												height="16"
												fill="currentColor"
												viewBox="0 0 16 16"
											>
												<path
													d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"
												/>
											</svg>
											{issue.state}
										</span>
									</dd>
								</dl>

								<dl class="grid sm:flex gap-x-3 text-sm">
									<dt class="min-w-36 max-w-[200px] text-gray-500 dark:text-neutral-500">
										Repository
									</dt>
									<dd class="font-medium font-mono text-gray-800 dark:text-neutral-200">
										{issue.repository['full_name']}
									</dd>
								</dl>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="flex-1 flex flex-col mb-4">
				<div class="flex-1 flex flex-col p-1.5 min-w-full inline-block align-middle">
					<div
						class="
          flex-1 flex flex-col bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden
         "
					>
						<div
							class="
            px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b
            border-gray-200 dark:border-neutral-700
          "
						>
							<div>
								<h2 class="font-semibold text-gray-800 dark:text-neutral-200">Summary</h2>
							</div>

							<div>
								<div class="inline-flex gap-x-2">
									<select
										id="model-select"
										bind:value={model}
										class="py-1 px-3 pe-9 block border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
									>
										<option selected="" value="transformers">Transformers</option>
										<option value="ollama">Ollama</option>
									</select>
								</div>
							</div>
						</div>
						{#if summary}
							<div class="flex-1 space-y-3 px-6 py-4 flex flex-col">
								<textarea
									class="py-3 px-4 block w-full flex-1 min-h-[10rem] border-gray-200 rounded-lg text-sm focus:border-blue-500 focus:ring-blue-500 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-neutral-400 dark:placeholder-neutral-500 dark:focus:ring-neutral-600"
									cols="6"
									placeholder=""
								>
									{summary}
								</textarea>
								<div class="flex items-center gap-2">
									<button
										on:click={() => {
											fetchSummary();
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
										Regenerate
									</button>
								</div>
							</div>
						{:else if loading}
							<div
								class="flex flex-auto flex-col min-h-[28rem] justify-center items-center p-4 md:p-5"
							>
								<div class="flex flex-col justify-center items-center">
									<p class="mb-2 text-sm text-gray-600 dark:text-neutral-400">
										Generating your summary...
									</p>
									<div
										class="animate-spin inline-block size-6 border-[3px] border-current border-t-transparent text-blue-600 rounded-full dark:text-blue-500"
										role="status"
										aria-label="loading"
									>
										<span class="sr-only">Loading...</span>
									</div>
								</div>
							</div>
						{:else}
							<div
								class="flex-1 max-w-sm w-full min-h-[28rem] flex flex-col justify-center items-center mx-auto px-6 py-4"
							>
								<h2 class="mt-5 font-semibold text-gray-800 dark:text-white">No summary yet</h2>
								<p class="mt-2 text-sm text-gray-600 dark:text-neutral-400">
									Use AI to summarize the issue.
								</p>
								<div class="mt-5 grid sm:flex gap-2">
									<button
										on:click={() => fetchSummary()}
										type="button"
										class="py-2 px-3 inline-flex justify-center items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
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
											class="flex-shrink-0 size-4"
											><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
												d="M6 21l15 -15l-3 -3l-15 15l3 3"
											/><path d="M15 6l3 3" /><path
												d="M9 3a2 2 0 0 0 2 2a2 2 0 0 0 -2 2a2 2 0 0 0 -2 -2a2 2 0 0 0 2 -2"
											/><path
												d="M19 13a2 2 0 0 0 2 2a2 2 0 0 0 -2 2a2 2 0 0 0 -2 -2a2 2 0 0 0 2 -2"
											/></svg
										>
										Generate
									</button>
								</div>
							</div>
						{/if}
					</div>
				</div>
			</div>
		</div>
		<div id="chat" class="">
			<Card title={'Chat'}>
				<Chat {issue} />
			</Card>
			<Card title={'Similar issues'}>
				{#if similarIssues.length > 0}
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th scope="col" class="px-6 py-3 text-start">
									<div class="flex items-center gap-x-2">
										<span class="text-xs font-semibold uppercase tracking-wide text-gray-800">
											Number
										</span>
									</div>
								</th>

								<th scope="col" class="px-6 py-3 text-start">
									<div class="flex items-center gap-x-2">
										<span class="text-xs font-semibold uppercase tracking-wide text-gray-800">
											Title
										</span>
									</div>
								</th>
							</tr>
						</thead>

						<tbody class="divide-y divide-gray-200">
							{#each similarIssues as issue}
								<tr class="bg-white hover:bg-gray-50">
									<td class="size-px whitespace-nowrap">
										<div>
											<span class="block px-6 py-2">
												<span>
													<span class="font-mono text-sm text-gray-600">#{issue.number}</span>
												</span>
											</span>
										</div>
									</td>
									<td class="size-px whitespace-nowrap">
										<span class="block px-6 py-2">
											<a href="/issues/{issue.public_id}" data-sveltekit-reload>
												<span class="text-sm text-blue-600">{issue.title}</span>
											</a>
										</span>
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				{:else}
					<div class="flex justify-center py-6">
						<EmptyState
							title={'No issues found.'}
							description={"Your search hasn't returned any results. Try another query."}
						/>
					</div>
				{/if}
			</Card>
		</div>
	</div>
{:else}
	<div class="flex flex-col gap-2 justify-center items-center h-full">
		<p class="mb-2 text-sm text-gray-600 dark:text-neutral-400">Loading issue...</p>
		<div
			class="animate-spin inline-block size-6 border-[3px] border-current border-t-transparent text-blue-600 rounded-full dark:text-blue-500"
			role="status"
			aria-label="loading"
		>
			<span class="sr-only">Loading...</span>
		</div>
	</div>
{/if}

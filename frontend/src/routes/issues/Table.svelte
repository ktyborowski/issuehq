<script>
	import Searchbox from './SearchBox.svelte';
	import TableRow from './TableRow.svelte';
	import { searches, issues } from '../../stores';
	import pluralize from 'pluralize';
	import EmptyState from '../../lib/EmptyState.svelte';

	export async function fetchSearches() {
		fetch('http://localhost:5000/searches')
			.then((response) => response.json())
			.then((data) => {
				searches.set(data);
			})
			.catch((error) => {
				return [];
			});
	}
</script>

<!-- Table Section -->
<div>
	<!-- Card -->
	<div class="flex flex-col">
		<div class="-m-1.5 overflow-x-auto">
			<div class="p-1.5 min-w-full inline-block align-middle">
				<div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
					<!-- Header -->
					<div
						class="px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b border-gray-200"
					>
						<div>
							<h2 class="text-xl font-semibold text-gray-800">Issues</h2>
							<p class="text-sm text-gray-600"></p>
						</div>

						<div>
							<div class="inline-flex gap-x-2">
								<button
									on:click={() => fetchSearches()}
									id="hs-as-table-table-export-dropdown"
									type="button"
									class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
									data-hs-overlay="#search-history-drawer"
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
											d="M12 8l0 4l2 2"
										/><path d="M3.05 11a9 9 0 1 1 .5 4m-.5 5v-5h5" /></svg
									>
									History
								</button>
								<button
									type="button"
									class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
									data-hs-overlay="#import-drawer"
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
											d="M12 5l0 14"
										/><path d="M5 12l14 0" /></svg
									>
									Import issues
								</button>
							</div>
						</div>
					</div>

					<div
						class="px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-b border-gray-200"
					>
						<div class="flex-1 max-w-2xl">
							<Searchbox />
						</div>

						<div>
							<button
								id="hs-as-table-table-export-dropdown"
								type="button"
								class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
								data-hs-overlay="#search-settings-drawer"
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
										d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"
									/><path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" /></svg
								>
								Settings
							</button>

							<button
								id="hs-as-table-table-filter-dropdown"
								type="button"
								class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-medium rounded-lg border border-gray-200 bg-white text-gray-800 shadow-sm hover:bg-gray-50 disabled:opacity-50 disabled:pointer-events-none dark:bg-neutral-900 dark:border-neutral-700 dark:text-white dark:hover:bg-neutral-800"
								data-hs-overlay="#search-filters-drawer"
							>
								<svg
									class="flex-shrink-0 size-3.5"
									xmlns="http://www.w3.org/2000/svg"
									width="24"
									height="24"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
									><path d="M3 6h18" /><path d="M7 12h10" /><path d="M10 18h4" /></svg
								>
								Filter
							</button>
						</div>
					</div>

					<!-- Table -->

					{#if $issues.length > 0}
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

									<th scope="col" class="px-6 py-3 text-start">
										<div class="flex items-center gap-x-2">
											<span class="text-xs font-semibold uppercase tracking-wide text-gray-800">
												Status
											</span>
										</div>
									</th>
								</tr>
							</thead>

							<tbody class="divide-y divide-gray-200">
								{#each $issues as issue}
									<TableRow {issue} />
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
					<!-- End Table -->

					<!-- Footer -->
					<div
						class="px-6 py-4 grid gap-3 md:flex md:justify-between md:items-center border-t border-gray-200"
					>
						<div>
							<p class="text-sm text-gray-600">
								<span class="font-semibold text-gray-800">{$issues.length}</span>
								{pluralize('result', $issues.length)}
							</p>
						</div>

						<div>
							<div class="inline-flex gap-x-2"></div>
						</div>
					</div>
					<!-- End Footer -->
				</div>
			</div>
		</div>
	</div>
	<!-- End Card -->
</div>
<!-- End Table Section -->

<!-- Modal -->
<div
	id="hs-ai-invoice-modal"
	class="hs-overlay hidden size-full fixed top-0 start-0 z-[80] overflow-x-hidden overflow-y-auto pointer-events-none"
>
	<div
		class="hs-overlay-open:mt-7 hs-overlay-open:opacity-100 hs-overlay-open:duration-500 mt-0 opacity-0 ease-out transition-all sm:max-w-lg sm:w-full m-3 sm:mx-auto"
	>
		<div class="relative flex flex-col bg-white shadow-lg rounded-xl pointer-events-auto">
			<div class="relative overflow-hidden min-h-32 bg-gray-900 text-center rounded-t-xl">
				<!-- Close Button -->
				<div class="absolute top-2 end-2">
					<button
						type="button"
						class="inline-flex flex-shrink-0 justify-center items-center size-8 rounded-lg text-gray-500 hover:text-gray-400 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 focus:ring-offset-gray-900 transition-all text-sm"
						data-hs-overlay="#hs-ai-invoice-modal"
					>
						<span class="sr-only">Close</span>
						<svg
							class="flex-shrink-0 size-4"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"><path d="M18 6 6 18" /><path d="m6 6 12 12" /></svg
						>
					</button>
				</div>
				<!-- End Close Button -->

				<!-- SVG Background Element -->
				<figure class="absolute inset-x-0 bottom-0">
					<svg
						preserveAspectRatio="none"
						xmlns="http://www.w3.org/2000/svg"
						x="0px"
						y="0px"
						viewBox="0 0 1920 100.1"
					>
						<path fill="currentColor" class="fill-white" d="M0,0c0,0,934.4,93.4,1920,0v100.1H0L0,0z"
						></path>
					</svg>
				</figure>
				<!-- End SVG Background Element -->
			</div>

			<div class="relative z-10 -mt-12">
				<!-- Icon -->
				<span
					class="mx-auto flex justify-center items-center size-[62px] rounded-full border border-gray-200 bg-white text-gray-700 shadow-sm"
				>
					<svg
						class="size-6"
						xmlns="http://www.w3.org/2000/svg"
						width="16"
						height="16"
						fill="currentColor"
						viewBox="0 0 16 16"
					>
						<path
							d="M1.92.506a.5.5 0 0 1 .434.14L3 1.293l.646-.647a.5.5 0 0 1 .708 0L5 1.293l.646-.647a.5.5 0 0 1 .708 0L7 1.293l.646-.647a.5.5 0 0 1 .708 0L9 1.293l.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .801.13l.5 1A.5.5 0 0 1 15 2v12a.5.5 0 0 1-.053.224l-.5 1a.5.5 0 0 1-.8.13L13 14.707l-.646.647a.5.5 0 0 1-.708 0L11 14.707l-.646.647a.5.5 0 0 1-.708 0L9 14.707l-.646.647a.5.5 0 0 1-.708 0L7 14.707l-.646.647a.5.5 0 0 1-.708 0L5 14.707l-.646.647a.5.5 0 0 1-.708 0L3 14.707l-.646.647a.5.5 0 0 1-.801-.13l-.5-1A.5.5 0 0 1 1 14V2a.5.5 0 0 1 .053-.224l.5-1a.5.5 0 0 1 .367-.27zm.217 1.338L2 2.118v11.764l.137.274.51-.51a.5.5 0 0 1 .707 0l.646.647.646-.646a.5.5 0 0 1 .708 0l.646.646.646-.646a.5.5 0 0 1 .708 0l.646.646.646-.646a.5.5 0 0 1 .708 0l.646.646.646-.646a.5.5 0 0 1 .708 0l.646.646.646-.646a.5.5 0 0 1 .708 0l.509.509.137-.274V2.118l-.137-.274-.51.51a.5.5 0 0 1-.707 0L12 1.707l-.646.647a.5.5 0 0 1-.708 0L10 1.707l-.646.647a.5.5 0 0 1-.708 0L8 1.707l-.646.647a.5.5 0 0 1-.708 0L6 1.707l-.646.647a.5.5 0 0 1-.708 0L4 1.707l-.646.647a.5.5 0 0 1-.708 0l-.509-.51z"
						/>
						<path
							d="M3 4.5a.5.5 0 0 1 .5-.5h6a.5.5 0 1 1 0 1h-6a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h6a.5.5 0 1 1 0 1h-6a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h6a.5.5 0 1 1 0 1h-6a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h6a.5.5 0 0 1 0 1h-6a.5.5 0 0 1-.5-.5zm8-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 0 1h-1a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 0 1h-1a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 0 1h-1a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 0 1h-1a.5.5 0 0 1-.5-.5z"
						/>
					</svg>
				</span>
				<!-- End Icon -->
			</div>

			<!-- Body -->
			<div class="p-4 sm:p-7 overflow-y-auto">
				<div class="text-center">
					<h3 class="text-lg font-semibold text-gray-800">Invoice from Preline</h3>
					<p class="text-sm text-gray-500">Invoice #3682303</p>
				</div>

				<!-- Grid -->
				<div class="mt-5 sm:mt-10 grid grid-cols-2 sm:grid-cols-3 gap-5">
					<div>
						<span class="block text-xs uppercase text-gray-500">Amount paid:</span>
						<span class="block text-sm font-medium text-gray-800">$316.8</span>
					</div>
					<!-- End Col -->

					<div>
						<span class="block text-xs uppercase text-gray-500">Date paid:</span>
						<span class="block text-sm font-medium text-gray-800">April 22, 2020</span>
					</div>
					<!-- End Col -->

					<div>
						<span class="block text-xs uppercase text-gray-500">Payment method:</span>
						<div class="flex items-center gap-x-2">
							<svg
								class="size-5"
								width="400"
								height="248"
								viewBox="0 0 400 248"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
							>
								<g clip-path="url(#clip0)">
									<path d="M254 220.8H146V26.4H254V220.8Z" fill="#FF5F00" />
									<path
										d="M152.8 123.6C152.8 84.2 171.2 49 200 26.4C178.2 9.2 151.4 0 123.6 0C55.4 0 0 55.4 0 123.6C0 191.8 55.4 247.2 123.6 247.2C151.4 247.2 178.2 238 200 220.8C171.2 198.2 152.8 163 152.8 123.6Z"
										fill="#EB001B"
									/>
									<path
										d="M400 123.6C400 191.8 344.6 247.2 276.4 247.2C248.6 247.2 221.8 238 200 220.8C228.8 198.2 247.2 163 247.2 123.6C247.2 84.2 228.8 49 200 26.4C221.8 9.2 248.6 0 276.4 0C344.6 0 400 55.4 400 123.6Z"
										fill="#F79E1B"
									/>
								</g>
								<defs>
									<clipPath id="clip0">
										<rect width="400" height="247.2" fill="white" />
									</clipPath>
								</defs>
							</svg>
							<span class="block text-sm font-medium text-gray-800">•••• 4242</span>
						</div>
					</div>
					<!-- End Col -->
				</div>
				<!-- End Grid -->

				<div class="mt-5 sm:mt-10">
					<h4 class="text-xs font-semibold uppercase text-gray-800">Summary</h4>

					<ul class="mt-3 flex flex-col">
						<li
							class="inline-flex items-center gap-x-2 py-3 px-4 text-sm border text-gray-800 -mt-px first:rounded-t-lg first:mt-0 last:rounded-b-lg"
						>
							<div class="flex items-center justify-between w-full">
								<span>Payment to Front</span>
								<span>$264.00</span>
							</div>
						</li>
						<li
							class="inline-flex items-center gap-x-2 py-3 px-4 text-sm border text-gray-800 -mt-px first:rounded-t-lg first:mt-0 last:rounded-b-lg"
						>
							<div class="flex items-center justify-between w-full">
								<span>Tax fee</span>
								<span>$52.8</span>
							</div>
						</li>
						<li
							class="inline-flex items-center gap-x-2 py-3 px-4 text-sm font-semibold bg-gray-50 border text-gray-800 -mt-px first:rounded-t-lg first:mt-0 last:rounded-b-lg"
						>
							<div class="flex items-center justify-between w-full">
								<span>Amount paid</span>
								<span>$316.8</span>
							</div>
						</li>
					</ul>
				</div>

				<!-- Button -->
				<div class="mt-5 flex justify-end gap-x-2">
					<a
						class="py-2 px-3 inline-flex justify-center items-center gap-2 rounded-lg border font-medium bg-white text-gray-700 shadow-sm align-middle hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-white focus:ring-blue-600 transition-all text-sm"
						href="#"
					>
						<svg
							class="flex-shrink-0 size-4"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><polyline
								points="7 10 12 15 17 10"
							/><line x1="12" x2="12" y1="15" y2="3" /></svg
						>
						Invoice PDF
					</a>
					<a
						class="py-2 px-3 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:pointer-events-none"
						href="#"
					>
						<svg
							class="flex-shrink-0 size-4"
							xmlns="http://www.w3.org/2000/svg"
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							stroke-linecap="round"
							stroke-linejoin="round"
							><polyline points="6 9 6 2 18 2 18 9" /><path
								d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"
							/><rect width="12" height="8" x="6" y="14" /></svg
						>
						Print
					</a>
				</div>
				<!-- End Buttons -->

				<div class="mt-5 sm:mt-10">
					<p class="text-sm text-gray-500">
						If you have any questions, please contact us at <a
							class="inline-flex items-center gap-x-1.5 text-blue-600 decoration-2 hover:underline font-medium"
							href="#">example@site.com</a
						>
						or call at
						<a
							class="inline-flex items-center gap-x-1.5 text-blue-600 decoration-2 hover:underline font-medium"
							href="tel:+1898345492">+1 898-34-5492</a
						>
					</p>
				</div>
			</div>
			<!-- End Body -->
		</div>
	</div>
</div>
<!-- End Modal -->

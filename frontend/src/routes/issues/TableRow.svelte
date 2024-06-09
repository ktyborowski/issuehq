<script>
	export let issue;
</script>

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
			<a href="/issues/{issue.public_id}">
				<span class="text-sm text-blue-600">{issue.title}</span>
			</a>
		</span>
	</td>
	<td class="size-px whitespace-nowrap">
		<span class="block px-6 py-2">
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
		</span>
	</td>
</tr>

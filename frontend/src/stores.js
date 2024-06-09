import { derived, writable } from 'svelte/store';

export const searchMode = writable('near_text');
export const searchQuery = writable('');

export const searches = writable([]);
export const issues = writable([]);

export const modeToName = {
	near_text: 'Semantic',
	bm25: 'Keyword',
	hybrid: 'Hybrid'
};
export const searchModeName = derived(searchMode, ($mode) => modeToName[$mode]);

export const loading = writable(false);

export async function fetchIssues(query, mode, limit, target, alpha, excludes, state) {
	loading.set(true);

	const searchParams = new URLSearchParams({
		query: query,
		limit: limit,
		mode: mode,
		target: target,
		alpha: alpha,
		state: state
	});

	excludes.forEach((exclude) => {
		searchParams.append('exclude', exclude);
	});

	const url = 'http://localhost:5000/issues/search?' + searchParams;
	fetch(url)
		.then((response) => response.json())
		.then((data) => {
			loading.set(false);
			issues.set(data);
		})
		.catch((error) => {
			loading.set(false);
			issues.set([]);
		});
}

export const selectedTarget = writable('title');

export const alpha = writable('0.5');

export const excludes = writable([]);

export const messages = writable([]);

export const selectedState = writable('open');

export const limit = writable('25');

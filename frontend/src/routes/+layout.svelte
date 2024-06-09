<script>
	import '../app.css';
	import { afterNavigate } from '$app/navigation';
	import Navbar from '../lib/Navbar.svelte';

	afterNavigate(() => {
		window.HSStaticMethods.autoInit();
	});
</script>

<Navbar />

<div
	class="max-w-screen-2xl max-h-full flex-1 flex flex-col px-4 py-10 sm:px-6 lg:px-8 lg:py-14 w-full mx-auto"
>
	<slot />
</div>

<style>
</style>

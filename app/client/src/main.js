import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		rows: 10,
		columns: 10
	}
});

export default app;
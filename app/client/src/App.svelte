<script>
	import { websocket, values } from "../store.js";
	import { io } from "socket.io-client";

	const socket = io();

	socket.on("connect", () => {
		console.log("connected with ID", socket.id);
		$websocket = socket;
	});

	socket.on("disconnect", () => {
		console.log("disconnected", socket.id);
		$websocket = null;
	});

	socket.on("setvalues", (vals) => {
		console.log("received", vals);
		$values = vals;
	});

	export let rows;
	export let columns;

	import Sheet from "./components/Sheet.svelte";
</script>

<main>
	<Sheet {rows} {columns} />
</main>

<style global>
	@import "milligram.min.css";
</style>

import { writable } from 'svelte/store';

export const websocket = writable({});
export const values = writable({});
export const selectedCell = writable("A1");

<script>
  import { values, selectedCell } from "../../store.js";

  export let rows;
  export let columns;

  $: cs = [...Array(columns).keys()].map((el) => el + 1);
  $: rs = [...Array(rows).keys()].map((el) => String.fromCharCode(65 + el));

  import Cell from "./Cell.svelte";
</script>

<div class="container">
  <div class="row">
    <div class="column column-50">
      <input type="text" bind:value={$values[$selectedCell]} />
    </div>
  </div>
  <div class="row">
    <table>
      <thead>
        <tr>
          <th />
          {#each cs as c}
            <th class="text-center">{c}</th>
          {/each}
        </tr>
      </thead>
      <tbody>
        {#each rs as r}
          <tr>
            <td class="text-center">{r}</td>
            {#each cs as c}
              <td><Cell pos="{r}{c}" /></td>
            {/each}
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>

<style>
  th,
  td {
    padding: 0;
    margin: 0;
    border: 1px solid lightgray;
  }

  tr > td {
    font-weight: bold;
  }

  .text-center {
    text-align: center;
  }
</style>

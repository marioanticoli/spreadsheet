<script>
    import { values, selectedCell, websocket } from "../../store.js";

    export let pos;

    $: content = $values[pos];
    $: result = calculateValue($values[pos]);
    $: shown = $selectedCell === pos ? content : result;

    /*** Event handlers */

    const handleBlur = (e) => updateValue(e.target.value.toUpperCase());

    const handleKeyUp = (e) => {
        if (e.keyCode === 13) {
            updateValue(e.target.value.toUpperCase());
        }
    };

    const setSelected = (e) => ($selectedCell = pos);

    /*** Helpers */

    const isValidInput = (value) =>
        value !== "" && value !== null && value !== undefined;

    const isNumber = (value) => /^-?\d+$/g.test(value);

    const isValidFormula = (value) => {
        const wellFormed = /^=(\w\d\+)*\w\d$/g.test(value);
        const selfReferent = value.substring(1).split("+").indexOf(pos) > -1;
        return wellFormed && !selfReferent;
    };

    const calculateFormula = (formula) =>
        formula.substring(1).split("+").reduce(reducer, 0);

    const reducer = (acc, cell) => {
        if (!isValidInput($values[cell])) {
            return acc;
        } else if (isNumber($values[cell])) {
            return acc + parseInt($values[cell]);
        } else if (isValidFormula($values[cell])) {
            const res = calculateFormula($values[cell]);
            if (res === "Error") return res;
            return acc + res;
        } else {
            return "Error";
        }
    };

    const calculateValue = (value) => {
        if (!isValidInput(value)) {
            delete $values[pos];
            return "";
        } else if (isNumber(value)) {
            return value;
        } else if (isValidFormula(value)) {
            return calculateFormula(value);
        } else {
            return "Error";
        }
    };

    const updateValue = (newValue) => {
        if (
            content !== newValue &&
            !(content === undefined && newValue === "")
        ) {
            $values[pos] = newValue;
            $websocket.emit("update", { cell: pos, value: newValue });
        }
    };
</script>

<input
    type="text"
    class="cell {$selectedCell === pos ? 'selected' : ''} {$values[
        $selectedCell
    ] !== undefined && $values[$selectedCell].indexOf(pos) > -1
        ? 'referenced-cell'
        : ''}"
    on:keyup={handleKeyUp}
    on:blur={handleBlur}
    on:focus={setSelected}
    bind:value={shown}
/>

<style>
    .selected {
        background-color: #d1dfe4;
    }

    .referenced-cell {
        background-color: rgb(196, 237, 196);
    }

    input {
        margin: 0;
        border: none;
        border-radius: 0;
    }
</style>

<script>
    export let value = '';
    export let placeholder = 'Enter text';
    export let disabled = false;
    export let width = '100%'; // Default width
    export let height = '150px'; // Default height

    const handleInput = (event) => {
        value = event.target.value;
    };
</script>

<textarea
    bind:value
    placeholder={placeholder}
    {disabled}
    on:input={handleInput}
    style="width: {width}; height: {height}; resize: both;"
></textarea>

<style>
    textarea {
        padding: 0.5rem;
        font-size: 1rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }

    textarea:focus {
        outline: none;
        border-color: #007bff;
    }

    textarea:disabled {
        background-color: #f5f5f5;
        cursor: not-allowed;
    }
</style>

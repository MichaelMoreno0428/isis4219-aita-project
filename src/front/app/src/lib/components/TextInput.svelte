<!-- src/lib/TextInput.svelte -->
<script lang="ts">
  export let value: string;
  export let placeholder = 'Enter text';
  export let disabled = false;
  export let width = '100%';
  export let height = '150px';

  const handleInput = (event) => {
    value = event.target.value;
  };
</script>

<textarea
  bind:value
  placeholder={placeholder}
  {disabled}
  on:input={handleInput}
  style="width: {width}; height: {height}; resize: vertical;"
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

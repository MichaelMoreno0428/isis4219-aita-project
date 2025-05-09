<script lang="ts">
  import { onDestroy } from 'svelte';
  import ModelSelector from './ModelSelector.svelte';
  import TextInput from './TextInput.svelte';

  let file: File | null = null;
  let resultUrl: string | null = null;
  let loading = false;

  const models = ['XMLBERT', 'HuggingFace', 'Classic ML', 'gpt-4o'];
  let selectedModel = models[0];

  onDestroy(() => {
    if (resultUrl) URL.revokeObjectURL(resultUrl);
  });

  async function upload() {
    if (!file || !selectedModel) return;
    loading = true;

    if (resultUrl) {
      URL.revokeObjectURL(resultUrl);
      resultUrl = null;
    }

    const form = new FormData();
    form.append('file', file);

    try {
      const res = await fetch(`http://localhost:8000/predict/${selectedModel}`, {
        method: 'POST',
        body: form,
      });

      if (!res.ok) {
        console.error('Upload failed', await res.text());
        return;
      }

      const blob = await res.blob();
      resultUrl = URL.createObjectURL(blob);
    } finally {
      loading = false;
    }
  }
</script>

<div class="container">
  <h1>r/AITA model prediction</h1>

  <ModelSelector
    {models}
    {selectedModel}
    onSelect={(model) => selectedModel = model}
  />

  <TextInput/>

  <button class="upload-button" on:click={upload} disabled={!file || loading}>
    {#if loading}Procesando{:else}Predecir{/if}
  </button>

  <!-- show the prediction here -->
</div>

<style>
  .container {
    max-width: 800px;
    margin: 2rem auto;
    text-align: center;
    font-family: system-ui, sans-serif;
    padding: 1rem;
  }
  h1 {
    margin-bottom: 1rem;
  }
  .upload-button {
    padding: 0.75rem 1.5rem;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    margin-bottom: 2rem;
  }
  .upload-button:disabled {
    background-color: #aaa;
    cursor: not-allowed;
  }
</style>
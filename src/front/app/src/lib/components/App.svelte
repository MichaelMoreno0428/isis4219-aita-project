<script lang="ts">
  import ModelSelector from './ModelSelector.svelte';
  import TextInput from './TextInput.svelte';
  let models = ['XMLBERT', 'HuggingFace', 'Classic ML', 'gpt-4o'];
  let selectedModel = models[0];
  let inputText = '';
let predictionResult: any = null;
  let loading = false;

  async function predict() {
    if (!inputText || !selectedModel) return;
    loading = true;
    predictionResult = null;

    try {
      const res = await fetch(`http://localhost:8000/predict/${selectedModel}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText }),
      });

      if (!res.ok) {
        console.error(await res.text());
        return;
      }

      const data = await res.json();
      predictionResult = data.result;
    } catch (e) {
      console.error(e);
    } finally {
      loading = false;
    }
  }
</script>

<div class="container">
  <h1>r/AITA Model Prediction</h1>

  <ModelSelector {models} {selectedModel} onSelect={(m) => selectedModel = m} />

  <TextInput bind:value={inputText} placeholder="Paste AITA post here..." />

  <button class="upload-button" on:click={predict} disabled={!inputText || loading}>
    {#if loading}Processing...{:else}Predict{/if}
  </button>

  {#if predictionResult}
    <div class="result">
      <h2>Prediction:</h2>
      {#if selectedModel === 'gpt-4o' || selectedModel === 'naive_bayes' || selectedModel === 'logistic_regression'}
        <p><strong>Etiqueta AITA:</strong> {predictionResult.etiqueta_aita}</p>
        <p><strong>Razonamiento:</strong> {predictionResult.razonamiento}</p>
      {:else}
        <p>{predictionResult}</p>
      {/if}
    </div>
  {/if}
</div>

<style>
  .container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 1rem;
    font-family: system-ui, sans-serif;
    text-align: center;
  }

  .upload-button {
    padding: 0.75rem 1.5rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    margin-top: 1rem;
    cursor: pointer;
  }

  .upload-button:disabled {
    background-color: #aaa;
    cursor: not-allowed;
  }

  .result {
    margin-top: 2rem;
    font-size: 1.25rem;
  }
</style>
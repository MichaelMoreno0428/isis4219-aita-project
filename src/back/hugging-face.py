from huggingface_hub import InferenceClient
import os

API_TOKEN = os.environ.get("HF_API_TOKEN")

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=API_TOKEN
)

prompt = "### Instruction:\nHow can I get from Colombia to Venezuela?\n\n### Response:\n"

response = client.text_generation(
    prompt=prompt,
    max_new_tokens=100,
    temperature=0.7,
    stream=False
)

print(response)


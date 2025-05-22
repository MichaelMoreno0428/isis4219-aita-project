from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextPayload(BaseModel):
    text: str

from openai import AzureOpenAI
DEFAULT_KEY = "PONERLALLAVE"
deployment_name = 'gpt'

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://invuniandesai-2.openai.azure.com/"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY", DEFAULT_KEY),
    api_version="2024-10-21"
)

@app.post("/predict/{model_name}")
async def predict_text(model_name: str, payload: TextPayload):
    text = payload.text
    # TODO
    if model_name == "Classic ML":
        result = "NTA"
    elif model_name == "HuggingFace":
        result = "YTA"
    elif model_name == "XMLBERT":
        result = "ESH"
    elif model_name == "gpt-4o":
        try:
            response = client.chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": "Actúa como un asistente de moderación que clasifica textos según las categorías del subreddit AITA. Tu respuesta debe estar en formato JSON con dos campos: 'etiqueta_aita', que puede ser una de las siguientes: YTA, NTA, ESH, INFO, y 'razonamiento', que es una explicación de por qué elegiste esa etiqueta. El razonamiento debe incluir un pequeño resumen de la situación analizada y una justificación clara y coherente. El formato de la respuesta debe ser estrictamente así:\n\n{\n  \"etiqueta_aita\": \"NTA\",\n  \"razonamiento\": \"El usuario explicó que su pareja no colaboró en las tareas del hogar, por lo tanto no es responsable del conflicto.\"\n}"},
                    {"role": "user", "content": text}
                ],
                temperature=0.6,
                max_tokens=100
            )
            result = response.choices[0].message.content.strip()
        except Exception as e:
            result = f"Error: {str(e)}"
    else:
        result = "Unknown model"

    return {"result": result, "text":text}

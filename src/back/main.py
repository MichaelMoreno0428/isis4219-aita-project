from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from gpt_client import get_aita_classification

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
        result = get_aita_classification(text)
    else:
        result = "Unknown model"

    return {"result": result, "text":text}

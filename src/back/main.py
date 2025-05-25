from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from gpt_client import get_aita_classification
from ml_classic import predict_with_logistic_regression, predict_with_naive_bayes

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

@app.get("/")
async def hello_world():
    return {"message": "Hello, world!"}

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
    elif model_name == "logistic_regression":
        result = predict_with_logistic_regression(text)
    elif model_name == "naive_bayes":
        result = predict_with_naive_bayes(text)
    else:
        result = "Unknown model"

    return {"result": result, "text":text}

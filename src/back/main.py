from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
        result = "INFO"
    else:
        result = "Unknown model"

    return {"result": result, "text":text}

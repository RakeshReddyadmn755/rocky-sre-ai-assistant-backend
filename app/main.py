
from fastapi import FastAPI
from pydantic import BaseModel
from openai_client import summarize_text

app = FastAPI()

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return summarize_text(input.text)

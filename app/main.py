# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.openai_client import summarize_text  # ← ✅ match your file structure

app = FastAPI()

# ✅ CORS middleware must come BEFORE routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, use your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return summarize_text(input.text)

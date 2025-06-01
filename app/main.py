from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.openai_client import summarize_text  # adjust if needed

app = FastAPI()  # ✅ Only define app ONCE

# ✅ CORS middleware must be applied to the same instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For security later, use your Vercel frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return summarize_text(input.text)

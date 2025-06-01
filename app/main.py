from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.openai_client import summarize_text  # or use .openai_client if you're inside /app

app = FastAPI()

# ✅ Enable CORS for frontend/backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific Vercel domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return summarize_text(input.text)

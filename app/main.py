
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add this CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your Vercel frontend URL for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from pydantic import BaseModel
from .openai_client import summarize_text

app = FastAPI()

class SREInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input: SREInput):
    return summarize_text(input.text)

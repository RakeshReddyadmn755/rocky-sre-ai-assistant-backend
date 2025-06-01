# app/openai_client.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str):
    prompt = f"""
    Format this into:
    What? So What? Now What? Owner? Due Date?
    Input: {text}
    Output:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    return {"summary": response.choices[0].message.content.strip()}

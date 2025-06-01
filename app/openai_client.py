import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str):
    if not client.api_key:
        raise ValueError("OpenAI API key not set")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use gpt-4 only if you have access
        messages=[
            {
                "role": "system",
                "content": "You are an SRE Assistant. Format the input into:\n- What\n- So What\n- Now What\n- Owner\n- Due Date"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.5
    )
    return {"summary": response.choices[0].message.content}

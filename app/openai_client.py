import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str):
    if not openai.api_key:
        raise ValueError("OpenAI API key not set")

    response = openai.ChatCompletion.create(
        model="gpt-4",
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
    return response.choices[0].message["content"]

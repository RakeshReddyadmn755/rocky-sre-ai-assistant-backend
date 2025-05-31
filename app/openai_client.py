
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str):
    prompt = f"""
    You are an SRE Assistant. Format the below input as:
    Category: <Win | Miss | Insight>
    What?: <summary>
    So What?: <impact>
    Now What?: <next steps>
    Owner: <team/person>
    Due Date: <target date>

    Input: {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message["content"]

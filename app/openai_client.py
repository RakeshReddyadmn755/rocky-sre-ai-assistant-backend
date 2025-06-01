import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str):
    if not openai.api_key:
        print("❌ OpenAI API key not set.")
        return {"error": "OpenAI API key not set."}

    try:
        print(f"📨 Input text: {text}")
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
        summary = response.choices[0].message["content"]
        print("✅ Response received.")
        return summary

    except Exception as e:
        print(f"❌ Error calling OpenAI API: {e}")
        return {"error": str(e)}

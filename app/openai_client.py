from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str):
    try:
        print(f"📨 Input text: {text}")
        response = client.chat.completions.create(
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
        summary = response.choices[0].message.content
        print("✅ Summary created.")
        return summary
    except Exception as e:
        print(f"❌ OpenAI error: {e}")
        return {"error": str(e)}

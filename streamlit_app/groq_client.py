import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama3-70b-8192"

SYSTEM_PROMPT = """
You are an enterprise NLP intent analysis assistant.

Return output strictly in JSON with:
{
  "answer": "...",
  "intent": "...",
  "confidence": 0.0-1.0,
  "entities": { "key": "value" }
}
"""

def call_groq(user_query, show_raw=False):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ]

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.2,
    )

    raw_output = completion.choices[0].message.content

    try:
        parsed = json.loads(raw_output)
    except:
        parsed = {
            "answer": raw_output,
            "intent": "UNKNOWN",
            "confidence": 0.5,
            "entities": {}
        }

    return parsed, raw_output if show_raw else None

from groq import Groq
import json

class ActionAgent:
    def __init__(self):
        self.client = Groq()

    def execute(self, query):
        prompt = f"""
Return ONLY JSON.

Supported actions:
create_ticket, schedule_meeting, apply_leave

User request:
{query}
"""

        res = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        try:
            return json.loads(res.choices[0].message.content)
        except:
            return {"error": "Invalid JSON"}

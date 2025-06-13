import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_gpt_response(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"

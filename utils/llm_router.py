# llm_router.py

from config import LLM_BACKEND
from secrets import OPENAI_API_KEY
import openai

# openai.api_key = OPENAI_API_KEY

def ask_openai(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a scholarly assistant providing interpretations of Greek linguistic data."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"


def ask_llm(prompt: str) -> str:
    if LLM_BACKEND == "openai":
        return ask_openai(prompt)
    elif LLM_BACKEND == "gemini":
        return ask_gemini(prompt)
    elif LLM_BACKEND == "grok":
        return ask_grok(prompt)
    else:
        return "[Error] Unknown LLM backend: " + LLM_BACKEND

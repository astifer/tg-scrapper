from openai import OpenAI
from dotenv import load_dotenv
import os

def create_summary(text: str, model: str="local") -> str:
    summary = ask_llm(text, model)
    return summary

def ask_llm(text: str, model: str = "gpt-3.5-turbo-0125") -> str:

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provide a summary for text below."},
            {
                "role": "user",
                "content": f"Отвечай только короткое саммари. Суммаризуй этот текст, выделяя ключевые технологии, людей и прочие важные вещи: {text}"
            }
        ]
    )

    return completion.choices[0].message.content


load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

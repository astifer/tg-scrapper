from transformers import AutoTokenizer, T5ForConditionalGeneration
from openai import OpenAI
from dotenv import load_dotenv
import os

def create_summary(text: str) -> str:
    text = "Суммаризируй: " + text
    input_ids = tokenizer(
        [text],
        max_length=1500,
        add_special_tokens=True,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=2
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary

def ask_llm(text: str) -> str:

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"{text}"
            }
        ]
    )

    return completion.choices[0].message


load_dotenv()

model_name = "rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name, local_files_only=True)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

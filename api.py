from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()
MODEL = "openai/gpt-oss-20b"

def ask(prompt, system="You are helpful.", temp=0, top_p=1, json_mode=False):
    options = {"response_format": {"type": "json_object"}} if json_mode else {}

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=temp,
        top_p=top_p,
        max_tokens=250,
        **options
    )
    return response.choices[0].message.content or ""

if __name__ == "__main__":
    print(ask("What is LLM"))
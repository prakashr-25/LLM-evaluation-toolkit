import tiktoken
import json

enc = tiktoken.get_encoding("cl100k_base")

texts = {
    "Sentence": "Artificial intelligence helps people solve problems.",
    "Paragraph": "LLMs understand and generate text. " * 20,
    "Page": "Transformers use attention to process information. " * 60,
    "JSON": json.dumps({"name": "Ravi", "skills": ["Python", "SQL"]}),
    "Tamil": "செயற்கை நுண்ணறிவு மனிதர்களுக்கு உதவுகிறது."
}

print("Text | Words | Tokens | Words/Token | 8K | 128K")

for name, value in texts.items():
    words = len(value.split())
    tokens = len(enc.encode(value))

    print(name, words, tokens, round(words / tokens, 2),
          tokens <= 8000, tokens <= 128000, sep=" | ")

def estimate_cost(input_tokens, output_tokens, price_in, price_out):
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000

chats = 1000 * 30
cost = estimate_cost(chats * 1500, chats * 400, 0.075, 0.30)

print(f"\nMonthly cost: ${cost:.3f}")
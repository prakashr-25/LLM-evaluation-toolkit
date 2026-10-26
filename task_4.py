from api import ask
from data.golden import tickets, resumes, problems
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
import csv
import json
import re
import time


def run(prompt, **options):
    time.sleep(3)
    return ask(prompt, **options)

def save(name, header, rows):
    with open("outputs/" + name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

Path("outputs/golden_tickets.json").write_text(
    json.dumps([{"text": t, "category": c, "priority": p}
                for t, c, p in tickets], indent=2))

Path("outputs/golden_resumes.json").write_text(
    json.dumps([{"text": t, "expected": e}
                for t, e in resumes], indent=2))


prompts = ["v1", "v2", "v3"]

rows = []
classification_results = []

for version in prompts:
    correct = 0
    system = Path(f"prompts/{version}.txt").read_text()

    for ticket, category, priority in tickets:
        answer = run("Ticket: " + ticket, system=system, temp=0)

        cat = re.search(r"\b(Billing|Technical|Account)\b", answer, re.I)
        pri = re.search(r"\b(Low|Medium|High)\b", answer, re.I)

        prediction = (cat.group().title(), pri.group().title()) if cat and pri else ("", "")
        passed = prediction == (category, priority)
        correct += passed

        rows.append([version, ticket, category, priority,
                     prediction[0], prediction[1], answer, passed])

    classification_results.append(f"{version}: {correct}/15 ({correct / 15:.0%})")
print(" | ".join(classification_results))

save("classification.csv",
     ["Version", "Ticket", "Category", "Priority",
      "Predicted Category", "Predicted Priority", "Response", "Correct"],
     rows)

rows = []

def final_number(answer):
    numbers = re.findall(r"-?\d+(?:\.\d+)?", answer)
    return float(numbers[-1]) if numbers else None

for question, expected in problems:
    plain = run(question + " Give only the final number.", temp=0)
    step = run(question + " Think step by step. Return only the final number.", temp=0)

    rows.append([question, expected, plain, step,
                 final_number(plain) == expected,
                 final_number(step) == expected])

save("reasoning.csv",
     ["Problem", "Expected", "Plain", "Step by Step",
      "Plain Correct", "Step Correct"], rows)

rows = []
creative = "Write one imaginative sentence advertising a solar-powered backpack."

for temp in [0, 0.7, 1.2]:
    for top_p in [0.3, 0.95]:
        answers = []

        for i in range(5):
            answer = run(creative, temp=temp, top_p=top_p)
            answers.append(answer)
            rows.append([temp, top_p, i + 1, answer])

        print(f"Temp {temp}, top_p {top_p}: {len(set(answers))}/5 unique")

save("creative.csv", ["Temperature", "Top P", "Run", "Response"], rows)

class Resume(BaseModel):
    name: str = Field(min_length=1)
    skills: list[str] = Field(min_length=1)
    years_experience: int = Field(ge=0, le=50)

rows = []
json_results = []

for json_mode in [False, True]:
    invalid = 0
    exact = 0

    for paragraph, expected in resumes:
        prompt = f"""Extract name, skills and years_experience.
Return a JSON object with those exact keys and no missing facts.
Resume: {paragraph}"""

        if not json_mode:
            prompt = "Extract the person's name, skills and experience: " + paragraph

        answer = run(prompt, json_mode=json_mode, temp=0)

        try:
            result = Resume.model_validate_json(answer).model_dump()
            match = result == expected
            exact += match
            valid = True
        except (ValidationError, ValueError):
            valid, match = False, False
            invalid += 1

        rows.append([json_mode, paragraph, json.dumps(expected),
                     answer, valid, match])

    mode = "JSON mode" if json_mode else "Plain"
    json_results.append(f"{mode}: {invalid}/5 invalid JSON")
print(" | ".join(json_results))

save("extraction.csv",
     ["JSON Mode", "Resume", "Expected", "Response", "Valid", "Exact Match"],
     rows)

bad_prompts = [
    ("Handle this", "Classify into Billing, Technical or Account with Low, Medium or High priority. Return JSON with category and priority.", "My card was charged twice."),
    ("Tell me about this", "Extract name, skills and years_experience as JSON. Do not invent details.", "Leena knows Python with 2 years of experience."),
    ("Write something", "Write two friendly sentences acknowledging a missing invoice. Do not promise a refund.", "My invoice is missing.")
]

rows = []

for i, (bad, good, sample) in enumerate(bad_prompts, 1):
    before = run(bad + "\n" + sample)
    after = run(good + "\n" + sample)
    rows.append([i, bad, good, before, after])
    print(f"\nPrompt {i}\nBefore: {before}\nAfter: {after}")

save("prompt_improvements.csv",
     ["Number", "Bad Prompt", "Improved Prompt", "Before", "After"], rows)
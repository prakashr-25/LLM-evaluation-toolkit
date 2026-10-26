from api import ask
import csv

tests = [
    ("Summarisation", "Summarise: Ravi ordered a laptop. Delivery was delayed by 3 days. He requested an update."),
    ("Classification", "Classify sentiment as positive or negative: The app crashes every day."),
    ("Extraction", "Extract name and skills: Asha knows Python and SQL."),
    ("Translation", "Translate to Tamil: Artificial intelligence is useful."),
    ("Code Generation", "Write Python code to add two numbers."),
    ("Knowledge Cutoff", "On 25 October 2026, how many workers were injured in the reported drone attack in Russia's Perm region? Do not browse."),
    ("Hallucination", "Summarise the 2025 paper 'Quantum Banana Networks' by Professor Zeno Cloudberry."),
    ("Hallucination Improved", "Summarise the 2025 paper 'Quantum Banana Networks' by Professor Zeno Cloudberry. Say I don't know if unsure."),
    ("Context Length", ""),
    ("Arithmetic", "There are 4 boxes with 12 pens each. 17 are sold and 9 added. How many remain?"),
    ("Logic", "All zips are zaps. All zaps are zops. Is every zip a zop?")
]

filler = "The report lists routine operations. " * 450
tests[8] = ("Context Length",
            filler + " Hidden code: LIME-482. " + filler +
            " What is the hidden code?")

with open("outputs/task_2_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Test", "Prompt", "Result", "Rating"])

    for name, prompt in tests:
        answer = ask(prompt)
        print(f"\n{name}: {answer}")
        rating = int(input("Rating (1-5): "))
        writer.writerow([name, prompt, answer, rating])
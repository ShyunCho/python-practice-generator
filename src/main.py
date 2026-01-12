from typing import Optional, List
import time
from src.generator import generate_questions
from src.grader import grade_questions
from src.utils import now_stamp, save_json


def ask_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a number.")

def ask_ops() -> List[str]:
    print("Choose operations (e.g., + - *). Example: + -")
    raw = input("Operations: ").strip().split()
    ops = [x for x in raw if x in {"+", "-", "*"}]
    return ops if ops else ["+"]

def ask_difficulty() -> str:
    while True:
        d = input("Difficulty (easy/medium/hard): ").strip().lower()
        if d in {"easy", "medium", "hard"}:
            return d
        print("Type: easy, medium, or hard.")

def main():
    print("\n=== Practice Generator ===")
    difficulty = ask_difficulty()
    ops = ask_ops()
    n = ask_int("Number of questions: ")

    questions = generate_questions(n=n, ops=ops, difficulty=difficulty)

    answers: List[Optional[int]] = []

    start = time.time()
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q.text()} = ?")
        ans = input("Your answer (blank to skip): ").strip()
        answers.append(int(ans) if ans else None)

    attempts = grade_questions(questions, answers)
    correct = sum(1 for a in attempts if a.is_correct)
    elapsed = int(time.time() - start)

    wrong = [
        {
            "question": a.question.text(),
            "your_answer": a.user_answer,
            "correct_answer": a.question.answer(),
        }
        for a in attempts
        if not a.is_correct
    ]

    report = {
        "difficulty": difficulty,
        "operations": ops,
        "total": n,
        "correct": correct,
        "score_pct": round(correct / n * 100, 1) if n else 0,
        "time_seconds": elapsed,
        "wrong": wrong,
    }

    filename = f"results/report_{now_stamp()}.json"
    save_json(filename, report)

    print("\n=== Result ===")
    print(f"Score: {correct}/{n} ({report['score_pct']}%)")
    print(f"Time: {elapsed}s")
    print(f"Saved: {filename}")

if __name__ == "__main__":
    main()

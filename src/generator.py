import random
from typing import List
from models import Question

DIFFICULTY_RANGES = {
    "easy": (1, 10),
    "medium": (10, 50),
    "hard": (50, 200),
}

def generate_questions(n: int, ops: List[str], difficulty: str) -> List[Question]:
    if difficulty not in DIFFICULTY_RANGES:
        raise ValueError("difficulty must be one of: easy, medium, hard")

    low, high = DIFFICULTY_RANGES[difficulty]
    questions: List[Question] = []

    for _ in range(n):
        op = random.choice(ops)
        a = random.randint(low, high)
        b = random.randint(low, high)

        # avoid negative results for subtraction
        if op == "-" and a < b:
            a, b = b, a

        questions.append(Question(a=a, b=b, op=op))

    return questions

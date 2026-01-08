from dataclasses import dataclass
from typing import Optional

@dataclass
class Question:
    a: int
    b: int
    op: str  # '+', '-', '*'

    def text(self) -> str:
        return f"{self.a} {self.op} {self.b}"

    def answer(self) -> int:
        if self.op == "+":
            return self.a + self.b
        if self.op == "-":
            return self.a - self.b
        if self.op == "*":
            return self.a * self.b
        raise ValueError(f"Unsupported operator: {self.op}")

@dataclass
class Attempt:
    question: Question
    user_answer: Optional[int]
    is_correct: bool

from typing import List
from src.models import Question, Attempt


def grade_questions(
    questions: List[Question],
    answers: list[int | None],
) -> List[Attempt]:
    attempts: List[Attempt] = []

    for question, user_answer in zip(questions, answers):
        is_correct = (
            user_answer == question.answer()
            if user_answer is not None
            else False
        )

        attempts.append(
            Attempt(
                question=question,
                user_answer=user_answer,
                is_correct=is_correct,
            )
        )

    return attempts

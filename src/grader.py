from typing import List, Optional
from src.models import Attempt, Question


def grade_questions(
    questions: List[Question], 
    answers: List[Optional[int]]
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

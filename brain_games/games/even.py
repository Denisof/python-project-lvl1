"""Implement Even game logic."""
import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
FROM_INT = 1
TO_INT = 1000


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    question = random.randint(FROM_INT, TO_INT)  # noqa:S311
    answer = 'yes' if _is_even(question) else 'no'
    return (question, answer)


def _is_even(number):
    """
    Check if number is even.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if even, False otherwise.
    """
    return number % 2 == 0

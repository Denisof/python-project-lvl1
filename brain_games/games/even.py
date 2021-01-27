"""Implement Even game logic."""
from random import randint

show_correct_answer = False
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    question = randint(1, 1000)  # noqa:S311
    answer = _is_even(question)
    return (question, answer)


def _is_even(number):
    """
    Check if number is even.

    Args:
        number (int): Number to check.

    Returns:
        string: yes if even, no otherwise.
    """
    return 'yes' if number % 2 == 0 else 'no'

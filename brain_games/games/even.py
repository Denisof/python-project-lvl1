"""Implement Even game logic."""
from random import randint


def get_rules():
    """
    Generate rules string.

    Returns:
        string: Rules string.
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    """
    Generate question.

    Returns:
        int: Random integer as a question.
    """
    return randint(1, 1000)  # noqa:S311


def is_correct(question, answer):
    """
    Check question and answer.

    Args:
        question (int): Number.
        answer (string): yes or no.

    Returns:
        bool: True if correct, False otherwise.
    """
    return answer == _is_even(question)


def _is_even(number):
    """
    Check if number is even.

    Args:
        number (int): Number to check.

    Returns:
        string: yes if even, no otherwise.
    """
    return 'yes' if number % 2 == 0 else 'no'

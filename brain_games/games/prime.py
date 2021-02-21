"""Implement Even game logic."""
import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_INT = 1
END_INT = 30


def get_question_and_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    question = random.randint(START_INT, END_INT)
    answer = 'yes' if _is_prime(question) else 'no'
    return (question, answer)


def _is_prime(number):
    """
    Check if number is prime.

    Args:
        number (int): Number to check.

    Returns:
        bool: True if prime, False otherwise.
    """
    if number <= 1:
        return False
    for divider in range(2, number // 2 + 1):
        if (number % divider) == 0:
            return False

    return True

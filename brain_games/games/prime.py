"""Implement Even game logic."""
from random import randint

SHOW_CORRECT_ANSWER = False
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_INT = 1
END_INT = 30


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    question = randint(START_INT, END_INT)  # noqa:S311
    answer = _is_prime(question)
    return (question, answer)


def _is_prime(number):
    """
    Check if number is prime.

    Args:
        number (int): Number to check.

    Returns:
        string: yes if prime, no otherwise.
    """
    if number > 1:
        for i in range(2, number // 2 + 1):  # noqa:WPS111
            if (number % i) == 0:
                return 'no'
    else:
        return 'no'

    return 'yes'

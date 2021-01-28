"""Implement Even game logic."""
from random import randint

SHOW_CORRECT_ANSWER = False
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    question = randint(1, 20)  # noqa:S311,WPS432,E501
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
        return 'yes'

    return 'yes'

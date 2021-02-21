"""Implement Nod game logic."""
import random

RULES = 'Find the greatest common divisor of given numbers..'
START_INT = 1
END_INT = 50


def get_question_and_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    first_num = random.randint(START_INT, END_INT)
    second_num = random.randint(START_INT, END_INT)
    question = '{0} {1}'.format(first_num, second_num)
    return (question, str(_find_gcd(first_num, second_num)))


def _find_gcd(first_num, second_num):
    """
    Colculate gratest common divisor.

    Args:
        first_num (int): First number.
        second_num (int): Second number.

    Returns:
        int: Greatest common devisor.
    """
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num  # noqa:WPS350
        else:
            second_num = second_num % first_num  # noqa:WPS350

    return first_num + second_num

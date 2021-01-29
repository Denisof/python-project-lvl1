"""Implement Nod game logic."""
from random import randint

SHOW_CORRECT_ANSWER = True
RULES = 'Find the greatest common divisor of given numbers..'
START_INT = 1
END_INT = 50


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    first_num = randint(START_INT, END_INT)  # noqa:S311
    second_num = randint(START_INT, END_INT)  # noqa:S311
    question = '{0} {1}'.format(first_num, second_num)  # noqa:S311
    return (question, str(_find_nod(first_num, second_num)))


def _find_nod(left, right):
    """
    Colculate gratest common divisor.

    Args:
        left (int): First number.
        right (int): Second number.

    Returns:
        int: Greatest common devisor.
    """
    while left != 0 and right != 0:
        if left > right:
            left = left % right  # noqa:WPS350
        else:
            right = right % left  # noqa:WPS350

    return left + right

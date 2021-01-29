"""Implement Calc game logic."""
from random import choice, randint

SHOW_CORRECT_ANSWER = False
RULES = 'What is the result of the expression?.'
START_INT = 1
TO_INT = 10
LAST_INT = 100


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    operrator = choice(('+', '-', '*'))  # noqa:S311
    left_operand = randint(TO_INT, LAST_INT)  # noqa:S311
    right_operand = randint(START_INT, TO_INT)  # noqa:S311
    question = '{0} {1} {2}'.format(left_operand, operrator, right_operand)
    return (question, str(eval(question)))  # noqa:WPS421,S307

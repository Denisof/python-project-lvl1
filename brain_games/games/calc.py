"""Implement Calc game logic."""
import operator
import random

RULES = 'What is the result of the expression?.'
START_INT = 1
TO_INT = 10
LAST_INT = 100
ADD = '+'
SUB = '-'
MUL = '*'


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    calc_funct_dict = {
        ADD: operator.add,
        SUB: operator.sub,
        MUL: operator.mul,
    }
    operation = random.choice((ADD, SUB, MUL))  # noqa:S311
    left_operand = random.randint(TO_INT, LAST_INT)  # noqa:S311
    right_operand = random.randint(START_INT, TO_INT)  # noqa:S311
    question = '{0} {1} {2}'.format(left_operand, operation, right_operand)
    return (
        question, str(calc_funct_dict[operation](left_operand, right_operand)),
    )  # noqa:WPS421,S307

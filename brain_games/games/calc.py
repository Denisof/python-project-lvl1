"""Implement Calc game logic."""
import operator
import random

RULES = 'What is the result of the expression?.'
START_NUMBER = 1
TO_NUMBER = 10
LAST_NUMBER = 100
ADD = '+'
SUB = '-'
MUL = '*'
calc_funcs_map = {
    ADD: operator.add,
    SUB: operator.sub,
    MUL: operator.mul,
}


def get_question_and_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    operation = random.choice((ADD, SUB, MUL))
    left_operand = random.randint(TO_NUMBER, LAST_NUMBER)
    right_operand = random.randint(START_NUMBER, TO_NUMBER)
    question = '{0} {1} {2}'.format(left_operand, operation, right_operand)
    current_operation = calc_funcs_map[operation]
    return (
        question, str(current_operation(left_operand, right_operand)),
    )  # noqa:S307

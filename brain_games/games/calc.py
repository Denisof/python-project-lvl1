"""Implement Calc game logic."""
from random import choice, randint

show_correct_answer = False
rules = 'What is the result of the expression?.'


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    operrator = choice(('+', '-', '*'))  # noqa:S311
    question = '{0} {1} {2}'.format(randint(50, 100), operrator, randint(1, 50))  # noqa:S311,WPS432,E501
    return (question, str(eval(question)))  # noqa:WPS421,S307

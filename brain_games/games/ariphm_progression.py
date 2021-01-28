"""Implement Ariphmetic progression game logic."""
from random import randint

SHOW_CORRECT_ANSWER = True
RULES = 'What number is missing in the progression?.'
_LENGTH = 10
_QUESTION_POSITION = randint(2, 10)  # noqa:S311,WPS432,E501


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    number = randint(1, 10)  # noqa:S311,WPS432,E501
    question = str(number)
    increment = randint(1, 10)  # noqa:S311,WPS432,E501
    incr = 1
    question = ''
    while incr <= _LENGTH:  # noqa:WPS111
        number += increment
        if (incr == _QUESTION_POSITION):
            question += ' {0}'  # noqa:WPS336
            answer = number
        else:
            question = ' '.join((question, str(number)))
        incr += 1
    return (question.format('..'), str(answer))  # noqa:WPS421,S307

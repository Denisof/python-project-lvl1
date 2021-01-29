"""Implement Ariphmetic progression game logic."""
from random import randint

SHOW_CORRECT_ANSWER = True
RULES = 'What number is missing in the progression?.'
_LENGTH = 10
_QUESTION_POS_SRART = 2
_QUESTION_POS_END = 10
_QUESTION_POS = randint(_QUESTION_POS_SRART, _QUESTION_POS_END)  # noqa:S311
_INCREMENT_START = 1
_INCREMENT_END = 10
_START_NUMBER_FROM = 1
_START_NUMBER_TO = 10
_increment = randint(_INCREMENT_START, _INCREMENT_END)  # noqa:S311


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    number = randint(_START_NUMBER_FROM, _START_NUMBER_TO)  # noqa:S311
    question = str(number)
    incr = 1
    question = ''
    while incr <= _LENGTH:  # noqa:WPS111
        number += _increment
        if (incr == _QUESTION_POS):
            question += ' {0}'  # noqa:WPS336
            answer = number
        else:
            if incr != 1:
                 question = ' '.join((question, str(number)))
            else:
                 question = ''.join((question, str(number)))          
        incr += 1
    return (question.format('..'), str(answer))  # noqa:WPS421,S307

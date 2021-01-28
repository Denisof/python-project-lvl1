"""Implement Ariphmetic progression game logic."""
from random import randint

show_correct_answer = True
rules = 'What number is missing in the progression?.'
_length = 10
_question_position = randint(2, 10)  # noqa:S311,WPS432,E501


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    number = randint(1, 10)  # noqa:S311,WPS432,E501
    question = (str(number))
    increment = randint(1, 10)  # noqa:S311,WPS432,E501
    incr = 1
    while incr <= _length:  # noqa:WPS111
        number += increment
        if (incr == _question_position):
            question = question + ('..')  # noqa:WPS336
            answer = number
        else:
            question = question + (str(number))
        incr += 1
    return (' '.join(question), str(answer))  # noqa:WPS421,S307

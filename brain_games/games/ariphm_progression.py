"""Implement Ariphmetic progression game logic."""
import random

RULES = 'What number is missing in the progression?.'
_LENGTH = 10
_QUESTION_POS_SRART = 2
_QUESTION_POS_END = 10
_QUESTION_POS = random.randint(  # noqa:S311
    _QUESTION_POS_SRART,
    _QUESTION_POS_END,
)
_INCREMENT_START = 1
_INCREMENT_END = 10
_START_NUMBER_FROM = 1
_START_NUMBER_TO = 10
_increment = random.randint(_INCREMENT_START, _INCREMENT_END)  # noqa:S311


def get_question_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    progression = list(map(str, get_progression(_increment)))
    return (
        '{0} .. {1}'.format(
            ' '.join(progression[:_QUESTION_POS]),
            ' '.join(progression[_QUESTION_POS + 1:]),
        ),
        progression[_QUESTION_POS],
    )


def get_progression(step):
    """
    Generate progression.

    Args:
        step (int): Step to build progession.

    Returns:
        Iterator: Progression iter.
    """
    start = random.randint(_START_NUMBER_FROM, _START_NUMBER_TO)  # noqa:S311
    end = step * _LENGTH + start
    return range(start, end, step)

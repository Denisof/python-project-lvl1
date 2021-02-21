"""Implement Ariphmetic progression game logic."""
import random

RULES = 'What number is missing in the progression?.'
_NUMS_IN_PROGRESSION_COUNT = 10
_QUESTION_POS_SRART = 2
_QUESTION_POS_END = 10
_QUESTION_POS = random.randint(
    _QUESTION_POS_SRART,
    _QUESTION_POS_END,
)
_INCREMENT_START = 1
_INCREMENT_END = 10
_START_NUMBER_FROM = 1
_START_NUMBER_TO = 10
_increment = random.randint(_INCREMENT_START, _INCREMENT_END)


def get_question_and_answer():
    """
    Generate question.

    Returns:
        tuple: Tuple of question and answer.
    """
    progression = list(map(str, get_progression(_increment)))
    nums_before_question = ' '.join(progression[:_QUESTION_POS])
    nums_after_question = ' '.join(progression[_QUESTION_POS + 1:])
    return (
        '{0} .. {1}'.format(
            nums_before_question,
            nums_after_question,
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
    start = random.randint(_START_NUMBER_FROM, _START_NUMBER_TO)
    end = step * _NUMS_IN_PROGRESSION_COUNT + start
    return range(start, end, step)

"""Implement Even game logic."""
from random import randint

from prompt import string


def play(player_name):
    """
    Plays a game with user in cli.

    Args:
        player_name (string): User name.
    """
    question_count = 3
    right_answers_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')  # noqa:WPS421, E501
    while right_answers_count < question_count:
        question_number = randint(1, 1000)  # noqa:S311
        print('Question: {0}'.format(question_number))  # noqa:WPS421
        answer = string('Your answer: ')
        if answer != _is_even(question_number):
            print("Let's try again, {0}!".format(player_name))  # noqa:WPS421
            return
        print('Correct!')  # noqa:WPS421
        right_answers_count += 1

    print('Congratulations, {0}!'.format(player_name))  # noqa:WPS421


def _is_even(number):
    return 'yes' if number % 2 == 0 else 'no'

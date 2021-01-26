"""Runs a game injected."""
from prompt import string

from brain_games.modules.cli_interaction import ask_name, greet_user
from brain_games.scripts.cli import welcome_user


def play(game):
    """
    Plays a game with user in cli.

    Args:
        game (brain_games.games): Game interface.
    """
    greet_user()
    name = ask_name()
    welcome_user(name)
    if not game:
        return
    question_count = 3
    right_answers_count = 0
    print(game.get_rules())  # noqa:WPS421
    while right_answers_count < question_count:
        question_answer = game.get_question_answer()
        print('Question: {0}'.format(question_answer[0]))  # noqa:WPS421
        user_answer = string('Your answer: ')
        if question_answer[1] != user_answer:
            print("Let's try again, {0}!".format(name))  # noqa:WPS421
            return
        print('Correct!')  # noqa:WPS421
        right_answers_count += 1

    print('Congratulations, {0}!'.format(name))  # noqa:WPS421

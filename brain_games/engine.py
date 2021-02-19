"""Runs a game injected."""
from prompt import string

QUESTION_COUNT = 3
_CORRECT_ANWER_TEMPLATE = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


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
    right_answers_count = 0
    print(game.RULES)  # noqa:WPS421
    while right_answers_count < QUESTION_COUNT:
        question_answer, correct_answer = game.get_question_answer()
        print('Question: {0}'.format(question_answer))  # noqa:WPS421
        user_answer = string('Your answer: ')
        if correct_answer != user_answer:
            print(_CORRECT_ANWER_TEMPLATE.format(  # noqa:WPS421
                user_answer,
                correct_answer,
            ),
            )
            print("Let's try again, {0}!".format(name))  # noqa:WPS421
            return
        print('Correct!')  # noqa:WPS421
        right_answers_count += 1

    print('Congratulations, {0}!'.format(name))  # noqa:WPS421


def ask_name():
    """
    Ask user a name in cli.

    Returns:
        string: Name provided by user
    """
    return string('May I have your name? ')


def greet_user():
    """Greet user in cli."""
    print('Welcome to the Brain Games!')  # noqa:WPS421


def welcome_user(name):
    """
    Welcomes user by name in cli.

    Args:
        name (string): User name.
    """
    print('Hello, {0}'.format(name))  # noqa:WPS421

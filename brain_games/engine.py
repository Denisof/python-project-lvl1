"""Runs a game injected."""
import prompt

ANSWERS_TO_WIN_COUNT = 3
_CORRECT_ANSWER_TEMPLATE = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def play(game):
    """
    Plays a game with user in cli.

    Args:
        game (brain_games.games): Game interface.
    """
    greet_user()
    name = ask_name()
    welcome_user(name)
    right_answers_count = 0
    print(game.RULES)
    while right_answers_count < ANSWERS_TO_WIN_COUNT:
        question, correct_answer = game.get_question_and_answer()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(_CORRECT_ANSWER_TEMPLATE.format(
                user_answer,
                correct_answer,
            ),
            )
            print("Let's try again, {0}!".format(name))
            return
        print('Correct!')
        right_answers_count += 1

    print('Congratulations, {0}!'.format(name))


def ask_name():
    """
    Ask user a name in cli.

    Returns:
        string: Name provided by user
    """
    return prompt.string('May I have your name? ')


def greet_user():
    """Greet user in cli."""
    print('Welcome to the Brain Games!')


def welcome_user(name):
    """
    Welcomes user by name in cli.

    Args:
        name (string): User name.
    """
    print('Hello, {0}'.format(name))

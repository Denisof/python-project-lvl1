"""Provide functions to interact with user in cli."""
from prompt import string


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

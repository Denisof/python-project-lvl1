"""Functions to interact with user in cli."""
from prompt import string


def welcome_user():
    """Welcomes user in cli."""
    name = string('May I have your name? ')
    print('Hello, {0}'.format(name))  # noqa:WPS421

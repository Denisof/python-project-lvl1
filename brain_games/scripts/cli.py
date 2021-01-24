"""Functions to interact with user in cli."""


def welcome_user(name):
    """
    Welcomes user by name in cli.

    Args:
        name (string): User name.
    """
    print('Hello, {0}'.format(name))  # noqa:WPS421

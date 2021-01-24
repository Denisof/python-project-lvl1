"""Expose even game entrypoint."""
# !/usr/bin/env python
from brain_games.modules.cli_interaction import ask_name, greet_user
from brain_games.modules.even_game import play
from brain_games.scripts.cli import welcome_user


def main():
    """Run main function."""
    greet_user()
    name = ask_name()
    welcome_user(name)
    play(name)


if __name__ == '__main__':
    main()

"""main file."""
# !/usr/bin/env python
from brain_games.engine import ask_name, greet_user, welcome_user


def main():
    """Run main function."""
    greet_user()
    welcome_user(ask_name())


if __name__ == '__main__':
    main()

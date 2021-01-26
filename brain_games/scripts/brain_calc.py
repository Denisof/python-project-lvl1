"""Expose calc game entrypoint."""
# !/usr/bin/env python
import brain_games.games.calc  # noqa:WPS301
from brain_games.games.engine import play


def main():
    """Run main function."""
    play(brain_games.games.calc)


if __name__ == '__main__':
    main()

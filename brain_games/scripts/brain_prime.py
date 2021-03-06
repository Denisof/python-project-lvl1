"""Expose prime game entrypoint."""
# !/usr/bin/env python
import brain_games.games.prime  # noqa:WPS301
from brain_games.engine import play


def main():
    """Run main function."""
    play(brain_games.games.prime)


if __name__ == '__main__':
    main()

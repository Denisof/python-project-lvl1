"""Expose nod game entrypoint."""
# !/usr/bin/env python
import brain_games.games.gcd  # noqa:WPS301
from brain_games.engine import play


def main():
    """Run main function."""
    play(brain_games.games.gcd)


if __name__ == '__main__':
    main()

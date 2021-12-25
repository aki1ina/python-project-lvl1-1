#!/usr/bin/env python3

"""The scripts start the game 'Brain-even'."""

from brain_games.engine import engine
from brain_games.games import even_number


def main():
    """
    Program start.
    Parameters are missing.
    Returns: None
    """
    engine(even_number)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""The scripts start the game 'Brain-calc'."""

from brain_games.engine import engine
from brain_games.games import brain_calc


def main():
    """
    Program start.
    Parameters are missing.
    Returns: None
    """
    engine(brain_calc)


if __name__ == '__main__':
    main()

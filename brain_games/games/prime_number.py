"""Function of the game 'Brain-game'"""

from random import randrange
from sympy import isprime

GAME_RULE = 'Answer "yes" if given number is prime, otherwise answer "no".'


def get_task_and_solution():
    """
    Get an integer(task) and correct answer.

    Parameters are missing.

    Returns:
        tuple:(int, str)
    """
    task = randrange(20)
    correct_answer = 'yes' if isprime(task) else 'no'

    return task, correct_answer

"""Function of the game 'Brain-game'"""

from random import randint
from sympy import isprime

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_and_solution():
    """
    Get an integer(task) and correct answer.

    Parameters are missing.

    Returns:
        tuple:(int, str)
    """
    task = randint(1, 20)
    correct_answer = 'yes' if isprime(task) else 'no'

    return task, correct_answer

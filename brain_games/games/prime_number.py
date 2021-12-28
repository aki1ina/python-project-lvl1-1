"""Function of the game 'Brain-game'"""

from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_and_solution():
    """
    Get an integer(task) and correct answer.

    Parameters are missing.

    Returns:
        tuple:(int, str)
    """
    task = randint(1, 20)
    correct_answer = 'yes' if is_prime(task) else 'no'

    return task, correct_answer


def is_prime(number):
    """
    Check the number for simplicity.

    Parameters:
        number: int

        Returns:
            bool
    """
    if (number < 2):
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1

    return True

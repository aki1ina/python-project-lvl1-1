
"""Functions of the game 'Brain-calc'."""

from random import randint, choice
from operator import add, sub, mul

GAME_RULE = 'What is the result of the expression?'
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_task_and_solution():
    """
    Get a mathematical expression (task) and correct answer.

    Parameters are missing.

    Returns:
        tuple: str
    """
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    random_operation = choice(OPERATIONS)

    correct_answer = random_operation[1](number1, number2)
    task = '{1} {0} {2}'.format(random_operation[0], number1, number2)

    return task, str(correct_answer)

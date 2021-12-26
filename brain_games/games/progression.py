
"""Functions of the game 'Brain-progression'."""

from random import randint, choice


GAME_RULE = 'What number is missing in the progression?'


def get_task_and_solution():
    """
    Get a tuple of integers (task) and a hidden number (correct answer)

    Parameters are missing.

    Returns:
        tuple: (str, int)
    """
    start, end, step = randint(0, 20), randint(40, 60), randint(2, 5)
    sequence = list(range(start, end, step))

    correct_answer = choice(sequence)
    task = ' '.join(
        '..' if number == correct_answer else str(number) for number in sequence
    )

    return task, str(correct_answer)

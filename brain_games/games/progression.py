from random import randint, randrange
import prompt


def item_search():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')
    i = 1
    counter_answer = 0
    while i <= 3:
        start = randint(0, 20)
        end = randint(40, 60)
        step = randint(2, 5)
        progression = list(range(start, end, step))
        len_progression = len(progression)
        index = randrange(len_progression)
        value = progression[index]
        progression[index] = '..'
        print('Question: ', progression)
        answer = prompt.string('Your answer: ')
        if int(answer) == value:
            print('Correct!')
            i += 1
            counter_answer += 1
        else:
            print("'{}'".format(answer), 'is wrong answer ;(. Correct answer was ' "'{}'.".format(value))
            print("Let's try again, {}!".format(name))
            break
    if counter_answer == 3:
        print('Congratulations, {}!'.format(name))

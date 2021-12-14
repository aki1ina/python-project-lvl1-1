import prompt
import math
from random import randint


def divider():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    i = 1
    counter_answer = 0
    res = ''
    while i <= 3:
        a = randint(0, 100)
        b = randint(0, 100)
        print('Question:', a, '', b)
        res = math.gcd(a, b)
        answer = prompt.string('Your answer: ')
        if res == int(answer):
            print('Correct!')
            i += 1
            counter_answer += 1
        else:
            print("'{}'".format(answer), 'is wrong answer ;(. Correct answer was ' "'{}'.".format(res))
            print("Let's try again, {}!".format(name))
            break
    if counter_answer == 3:
        print('Congratulations, {}!'.format(name))

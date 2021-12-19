import prompt
from random import randrange
from sympy import isprime


def prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    counter_answer = 0
    while i <= 3:
        a = randrange(20)
        print('Question:', a)
        answer = prompt.string('Your answer: ')
        if isprime(a) is True and answer == "yes":
            print('Correct!')
            i += 1
            counter_answer += 1
        elif isprime(a) is False and answer == "no":
            print('Correct!')
            i += 1
            counter_answer += 1
        elif isprime(a) is True and answer == "no":
            print('"no" is wrong answer ;(. Correct answer was "yes". ')
            print("Let's try again, {}!".format(name))
            break
        elif isprime(a) is False and answer == "yes":
            print('"yes" is wrong answer ;(. Correct answer was "no". ')
            print("Let's try again, {}!".format(name))
            break
    if counter_answer == 3:
        print('Congratulations, {}!'.format(name))

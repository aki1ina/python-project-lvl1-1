import prompt
from random import randint, choice


def calculator():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 1
    counter_answer = 0
    while i <= 3:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        operator = choice(['-', '+', '*'])
        print('Question:', str(number1), str(operator), str(number2))
        if operator == '+':
            solution = number1 + number2
        elif operator == '-':
            solution = number1 - number2
        else:
            solution = number1 * number2
        answer = prompt.string('Your answer: ')
        if solution == int(answer):
            print('Correct!')
            i += 1
            counter_answer += 1
        else:
            print("'{}'".format(answer), 'is wrong answer ;(. Correct answer was ' "'{}'.".format(solution))
            print("Let's try again, {}!".format(name))
            break
    if counter_answer == 3:
        print('Congratulations, {}!'.format(name))

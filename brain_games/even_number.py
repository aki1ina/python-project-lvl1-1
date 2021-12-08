import prompt
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    c = 0
    while i <= 3:
        number = randint(0, 100)
        print('Question:', number)
        module = number % 2
        answer = prompt.string('Your answer: ')
        if module == 0 and answer == 'yes':
            print('Correct!')
            i += 1
            c += 1
        elif module != 0 and answer == 'no':
            print('Correct!')
            i += 1
            c += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, {}".format(name))
            break
    if c == 3:
        print('Congratulations, {}!'.format(name))

        

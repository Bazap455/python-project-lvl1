#!/usr/bin/env python


from random import randint


def main(name):
    n = 3   # Number of rounds
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while n > 0:
        random_number = randint(1, 100)
        print('Question:', random_number)
        answer = str(input())
        print('Your answer:', answer)

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            n -= 1
            print('Correct!')
        else:
            print("'", answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
            print('Correct answer was ', "'", correct_answer, "'.", sep='')
            print('Let`s try again, ', name, '!', sep='')
            break

        if n == 0:
            print('Congratulations, ', name, '!', sep='')


if __name__ == '__main__':
    main('User_name')

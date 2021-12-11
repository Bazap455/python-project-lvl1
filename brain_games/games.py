#!/usr/bin/env python


from random import randint
from . import main_functions


def even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = main_functions.number_of_rounds()

    for i in range(n):
        random_number = randint(1, 100)
        correct_answer = main_functions.even_test(random_number)
        user_answer = main_functions.ask_user(random_number)

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


def calc(name):
    print('What is the result of the expression?')
    n = main_functions.number_of_rounds()

    for i in range(n):
        a = randint(1, 10)
        b = randint(1, 10)
        correct_answer, task = main_functions.answer_and_task_for_calc(a, b)
        user_answer = int(main_functions.ask_user(task))

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


def gcd(name):
    print('Find the greatest common divisor of given numbers.')
    n = main_functions.number_of_rounds()

    for i in range(n):
        a = randint(1, 20)
        b = randint(1, 20)
        task = str(a) + ' ' + str(b)
        correct_answer = main_functions.gcd(a, b)
        user_answer = int(main_functions.ask_user(task))

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


def progression(name):
    print('What number is missing in the progression?')
    n = main_functions.number_of_rounds()

    for i in range(n):
        length = randint(5, 10)
        hidden_pos = randint(1, length)
        correct_answer, task = main_functions.progression(length, hidden_pos)
        user_answer = int(main_functions.ask_user(task))

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


if __name__ == '__main__':
    print('Choose a game!')

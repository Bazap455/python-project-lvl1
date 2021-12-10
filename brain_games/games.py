#!/usr/bin/env python


from random import randint
from . import main_functions
# from main_functions import print_game_info


def even(name):
    main_functions.print_game_info()
    n = main_functions.number_of_rounds()

    for i in range(n):
        random_number = randint(1, 100)
        user_answer = main_functions.ask_user(random_number)
        correct_answer = main_functions.even_test(random_number)

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


def calc(name):
    main_functions.print_game_info()
    n = main_functions.number_of_rounds()

    for i in range(n):
        a = randint(1, 10)
        b = randint(1, 10)
        task_number = randint(1, 3)

        if task_number == 1:
            task = str(a) + '+' + str(b)
            correct_answer = str(a + b)

        if task_number == 2:
            task = str(a) + '-' + str(b)
            correct_answer = str(a - b)

        if task_number == 3:
            task = str(a) + '*' + str(b)
            correct_answer = str(a * b)

        user_answer = main_functions.ask_user(task)

        if not main_functions.check(user_answer, correct_answer):
            print('Let`s try again, ', name, '!', sep='')
            break

        if i == n - 1:
            print('Congratulations, ', name, '!', sep='')


if __name__ == '__main__':
    print('Choose a game!')

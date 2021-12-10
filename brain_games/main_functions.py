#!/usr/bin/env python

from random import randint


def print_game_info():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def number_of_rounds():
    n = 3   # Number of rounds
    return(n)


def ask_user(task):
    print('Question:', task)
    user_answer = str(input())
    print('Your answer:', user_answer)
    return(user_answer)


def even_test(num):
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return(correct_answer)


def answer_for_calc(a, b):
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

    return(correct_answer, task)


def check(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return(True)
    else:
        print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
        print('Correct answer was ', "'", correct_answer, "'.", sep='')
        return(False)

#!/usr/bin/env python

from random import randint


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


def answer_and_task_for_calc(a, b):
    task_number = randint(1, 3)

    if task_number == 1:
        task = str(a) + '+' + str(b)
        correct_answer = a + b

    if task_number == 2:
        task = str(a) + '-' + str(b)
        correct_answer = a - b

    if task_number == 3:
        task = str(a) + '*' + str(b)
        correct_answer = a * b

    return(correct_answer, task)


def gcd(a, b):

    if b > a:
        a, b = b, a

    r = a % b

    while r:
        a, b = b, r
        r = a % b

    return(b)


def check(user_answer, correct_answer):

    if user_answer == correct_answer:
        print('Correct!')
        return(True)
    else:
        print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
        print('Correct answer was ', "'", correct_answer, "'.", sep='')
        return(False)

#!/usr/bin/env python

from random import randint


def number_of_rounds():
    n = 3   # Number of rounds
    return(n)


def ask_user(task):
    print('Question:', task)
    user_answer = str(input())
    user_answer = user_answer.strip(' ') # Delet extra spaces
    user_answer = user_answer.lower()
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


def progression(length, hidden_pos):
    a = randint(1, 10)
    d = randint(1, 10)
    progression = []
    task = ''

    for i in range(1, length + 1):
        progression.append(a)
        a += d

        if i == hidden_pos:
            task += '.. '
            hidden_number = a
        else:
            task += str(a) + ' '

    return(hidden_number, task)


def check(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == correct_answer:
        print('Correct!')
        return(True)
    else:
        print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
        print('Correct answer was ', "'", correct_answer, "'.", sep='')
        return(False)

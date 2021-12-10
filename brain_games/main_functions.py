#!/usr/bin/env python


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


def check(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return(True)
    else:
        print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
        print('Correct answer was ', "'", correct_answer, "'.", sep='')
        return(False)

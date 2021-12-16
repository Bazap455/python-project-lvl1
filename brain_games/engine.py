#!/usr/bin/env python

from random import randint


NUMBER_OF_ROUNDS = 3   # Number of rounds


def ask_user(task):
    print('Question:', task)


def get_user_answer():
    user_answer = str(input())
    user_answer = user_answer.strip(' ')    # Delet extra spaces.
    user_answer = user_answer.lower()       # Input is case insensitive.
    print('Your answer:', user_answer)
    return(user_answer)


def check_answer(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == correct_answer:
        return(True)
    else:
        return(False)


def next_round():
    print('Correct!')


def game_over(username, user_answer, correct_answer):
    print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
    print('Correct answer was ', "'", correct_answer, "'.", sep='')
    print("Let's try again, ", username, '!', sep='')


def user_win(username):
    print('Congratulations, ', username, '!', sep='')
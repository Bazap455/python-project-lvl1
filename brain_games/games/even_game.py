#!/usr/bin/env python


from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):

    if num % 2 == 0:
        return True
    else:
        return False


def generate_round():
    num = randint(1, 100)
    task = str(num)
    if is_even(num):
        return 'yes', task
    else:
        return 'no', task

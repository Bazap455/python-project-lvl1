#!/usr/bin/env python


from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


def generate_round():
    num = randint(1, 40)
    if is_prime(num):
        return 'yes', num
    else:
        return 'no', num

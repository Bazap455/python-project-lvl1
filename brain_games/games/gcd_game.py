#!/usr/bin/env python


from random import randint


TEXT_OF_RULES = 'Find the greatest common divisor of given numbers.'
min_num = 1       # Lower limit of the range of numbers used in the game
max_num = 20      # Upper limit of the range of numbers used in the game.


def gcd(a, b):

    if b > a:
        a, b = b, a

    r = a % b

    while r:
        a, b = b, r
        r = a % b

    return(b)


def main():
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
    correct_answer = gcd(a, b)
    task = str(a) + ' ' + str(b)
    return correct_answer, task


if __name__ == '__main__':
    main('username')

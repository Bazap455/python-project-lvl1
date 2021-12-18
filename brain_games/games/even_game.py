#!/usr/bin/env python


from random import randint


TEXT_OF_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
min_num = 1       # Lower limit of the range of numbers used in the game
max_num = 100     # Upper limit of the range of numbers used in the game.


def even_test(num):

    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return(correct_answer)


def main():
    num = randint(min_num, max_num)
    correct_answer = even_test(num)
    task = str(num)
    return correct_answer, task


if __name__ == '__main__':
    main('username')

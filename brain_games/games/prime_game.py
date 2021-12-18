#!/usr/bin/env python


from random import randint

TEXT_OF_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
list_of_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
max_num = 40     # Max number in the game.


def prime_test(number):

    if number in list_of_prime_numbers:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return(correct_answer)


def main():
    task = randint(1, max_num)
    correct_answer = prime_test(task)
    return correct_answer, task


if __name__ == '__main__':
    main('username')

#!/usr/bin/env python


from random import randint


TEXT_OF_RULES = 'What is the result of the expression?'
min_num = 1       # Lower limit of the range of numbers used in the game
max_num = 10      # Upper limit of the range of numbers used in the game.


def main():
    a = randint(min_num, max_num)
    b = randint(min_num, max_num)
    task_number = randint(1, 3)

    if task_number == 1:
        task = str(a) + ' + ' + str(b)
        correct_answer = a + b

    if task_number == 2:
        task = str(a) + ' - ' + str(b)
        correct_answer = a - b

    if task_number == 3:
        task = str(a) + ' * ' + str(b)
        correct_answer = a * b

    return(correct_answer, task)


if __name__ == '__main__':
    main('username')

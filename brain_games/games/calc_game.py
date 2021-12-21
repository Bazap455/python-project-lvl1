#!/usr/bin/env python


from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    a = randint(1, 10)
    b = randint(1, 10)
    list_of_operations = [('+', add), ('-', sub), ('*', mul)]
    operation, function = choice(list_of_operations)
    task = f'{a} {operation} {b}'
    correct_answer = function(a, b)
    return correct_answer, task

from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    a = randint(1, 10)
    b = randint(1, 10)
    operations_and_function = [('+', add), ('-', sub), ('*', mul)]
    operation, function = choice(operations_and_function)
    question = f'{a} {operation} {b}'
    correct_answer = function(a, b)
    correct_answer = str(correct_answer)
    return correct_answer, question

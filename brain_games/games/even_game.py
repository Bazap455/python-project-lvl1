from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):

    return num % 2 == 0


def generate_round():
    num = randint(1, 100)
    question = str(num)
    if is_even(num):
        answer_and_task = ('yes', question)        
    else:
        answer_and_task = ('no', question)
    return answer_and_task

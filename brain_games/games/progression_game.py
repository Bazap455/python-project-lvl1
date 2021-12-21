#!/usr/bin/env python


from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    a1 = randint(1, 10)     # First member of progression.
    d = randint(1, 10)      # Difference of successive members
    length = randint(5, 10)
    hidden_pos = randint(1, length)
    progression = []

    for i in range(1, length + 1):
        ai = a1 + (i - 1) * d

        if i == hidden_pos:
            progression.append("..")
            correct_answer = ai
        else:
            progression.append(str(ai))

    task = " ".join(progression)
    return correct_answer, task

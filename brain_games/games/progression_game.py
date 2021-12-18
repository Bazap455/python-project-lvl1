#!/usr/bin/env python


from random import randint


TEXT_OF_RULES = 'What number is missing in the progression?'
min_num = 5       # The smallest number of members in a progression.
max_num = 10      # The biggest number of members in a progression.


def get_progression(a1, d, length):
    a = a1
    progression = []

    for i in range(1, length + 1):
        progression.append(a)
        a += d

    return(progression)


def get_task(progression, hidden_pos):
    task = ''

    for i in range(1, len(progression) + 1):

        if i == hidden_pos:
            task += '.. '
        else:
            task += str(progression[i - 1]) + ' '

    return(task)


def main():
    a1 = randint(1, 10)     # First member of progression.
    d = randint(1, 10)      # Difference of successive members
    length = randint(min_num, max_num)
    hidden_pos = randint(1, length)
    progression = get_progression(a1, d, length)
    task = get_task(progression, hidden_pos)
    correct_answer = progression[hidden_pos - 1]
    return correct_answer, task


if __name__ == '__main__':
    main('username')

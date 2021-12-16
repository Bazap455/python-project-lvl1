#!/usr/bin/env python


from random import randint
from brain_games import engine


text_of_rules = 'What number is missing in the progression?'
n = engine.NUMBER_OF_ROUNDS
A = 5       # The smallest number of members in a progression.
B = 10      # The biggest number of members in a progression.
A1 = randint(1, 10)     # First member of progression.
D = randint(1, 10)      # Difference of successive members


def get_progression(length):
    a = A1
    progression = []

    for i in range(1, length + 1):
        progression.append(a)
        a += D
    
    return(progression)


def get_task(progression, hidden_pos):
    task = ''

    for i in range(1, len(progression) + 1):

        if i == hidden_pos:
            task += '.. '
        else:
            task += str(progression[i - 1]) + ' '
    
    return(task)


def get_correct_answer(progression, hidden_pos):
    correct_answer = progression[hidden_pos - 1]
    return(correct_answer)


def main(username):

    for i in range(n):
        length = randint(A, B)
        hidden_pos = randint(1, length)
        progression = get_progression(length)
        task = get_task(progression, hidden_pos)
        correct_answer = get_correct_answer(progression, hidden_pos)
        engine.ask_user(task)
        user_answer = engine.get_user_answer()
        result = engine.check_answer(user_answer, correct_answer)

        if result:
            engine.next_round()
            continue
        else:
            engine.game_over(username, user_answer, correct_answer)
            break
    else:
        engine.user_win(username)


if __name__ == '__main__':
    main('username')

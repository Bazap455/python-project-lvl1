#!/usr/bin/env python


from random import randint
from brain_games import engine

text_of_rules = 'What is the result of the expression?'
n = engine.NUMBER_OF_ROUNDS
A = 1       # Lower limit of the range of numbers used in the game
B = 10      # Upper limit of the range of numbers used in the game.


def get_correct_answer_and_task(a, b):
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


def main(username):

    for i in range(n):
        a = randint(A, B)
        b = randint(A, B)
        correct_answer, task = get_correct_answer_and_task(a, b)
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

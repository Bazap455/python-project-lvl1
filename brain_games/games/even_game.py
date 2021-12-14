#!/usr/bin/env python


from random import randint
from brain_games import engine


text_of_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
n = engine.NUMBER_OF_ROUNDS
A = 1       # Lower limit of the range of numbers used in the game
B = 100     # Upper limit of the range of numbers used in the game.


def get_correct_answer():
    correct_answer = randint(A, B)
    return correct_answer


def get_text_of_task(correct_answer):
    text_of_task = str(correct_answer)
    return text_of_task


def main(username):

    for i in range(n):
        correct_answer = get_correct_answer()
        task = get_text_of_task(correct_answer)
        engine.ask_user(task)
        user_answer = engine.get_user_answer()
        result = engine.check_answer(user_answer, correct_answer)

        if result:
            engine.next_round()
            continue
        else:
            engine.game_over(username)
            break


if __name__ == '__main__':
    main('username')

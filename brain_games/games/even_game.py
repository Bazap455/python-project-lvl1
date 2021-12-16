#!/usr/bin/env python


from random import randint
from brain_games import engine


text_of_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
n = engine.NUMBER_OF_ROUNDS
A = 1       # Lower limit of the range of numbers used in the game
B = 100     # Upper limit of the range of numbers used in the game.


def even_test(num):

    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return(correct_answer)


def main(username):

    for i in range(n):
        num = randint(A, B)
        correct_answer = even_test(num)
        task = str(num)
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

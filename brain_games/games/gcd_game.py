#!/usr/bin/env python


from random import randint
from brain_games import engine


text_of_rules = 'Find the greatest common divisor of given numbers.'
n = engine.NUMBER_OF_ROUNDS
A = 1       # Lower limit of the range of numbers used in the game
B = 20      # Upper limit of the range of numbers used in the game.


def gcd(a, b):

    if b > a:
        a, b = b, a

    r = a % b

    while r:
        a, b = b, r
        r = a % b

    return(b)


def main(username):

    for i in range(n):
        a = randint(A, B)
        b = randint(A, B)
        correct_answer = gcd(a, b)
        task = str(a) + ' ' + str(b)
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

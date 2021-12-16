#!/usr/bin/env python


from random import randint
from brain_games import engine

text_of_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
n = engine.NUMBER_OF_ROUNDS
list_of_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
MAX_NUMBER = 40     # Max number in the game.


def prime_test(number):
    
    if number in list_of_prime_numbers:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    
    return(correct_answer)


def main(username):

    for i in range(n):
        task = randint(1, MAX_NUMBER)
        correct_answer = prime_test(task)
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

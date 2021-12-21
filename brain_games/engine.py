#!/usr/bin/env python


from brain_games import cli


n = 3   # Number of rounds


def run(game):
    username = cli.welcome_user()
    print(game.DESCRIPTION)

    for i in range(n):
        correct_answer, task = game.generate_round()
        print('Question:', task)
        user_answer = str(input())
        user_answer = user_answer.strip(' ')    # Delet extra spaces.
        user_answer = user_answer.lower()       # Input is case insensitive.
        print('Your answer:', user_answer)
        correct_answer = str(correct_answer)

        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            template = "'{}' is wrong answer ;(. Correct answer was '{}'.\n\
Let's try again, {}!"
            print(template.format(user_answer, correct_answer, username))
            break

    else:
        template = "Congratulations, {}!"
        print(template.format(username))

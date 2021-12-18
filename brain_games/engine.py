#!/usr/bin/env python


from brain_games import welcome_user


def get_user_answer():
    user_answer = str(input())
    user_answer = user_answer.strip(' ')    # Delet extra spaces.
    user_answer = user_answer.lower()       # Input is case insensitive.
    print('Your answer:', user_answer)
    return(user_answer)


def check_answer(user_answer, correct_answer):
    correct_answer = str(correct_answer)

    if user_answer == correct_answer:
        return(True)
    else:
        return(False)


def game_over(username, user_answer, correct_answer):
    print("'", user_answer, "' ", 'is wrong answer ;(.', sep='', end=' ')
    print('Correct answer was ', "'", correct_answer, "'.", sep='')
    print("Let's try again, ", username, '!', sep='')


def run(game):
    n = 3   # Number of rounds
    username = welcome_user.get_username()
    print(game.TEXT_OF_RULES)

    for i in range(n):
        correct_answer, task = game.main()
        print('Question:', task)
        user_answer = get_user_answer()
        result = check_answer(user_answer, correct_answer)

        if result:
            print('Correct!')
            continue
        else:
            game_over(username, user_answer, correct_answer)
            break
    else:
        print('Congratulations, ', username, '!', sep='')

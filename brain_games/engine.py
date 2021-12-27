from brain_games import cli


NUMBER_OF_ROUNDS = 3


def run(game):
    username = cli.welcome_user()
    print(game.DESCRIPTION)

    for i in range(NUMBER_OF_ROUNDS):
        correct_answer, question = game.generate_round()
        print('Question:', question)
        user_answer = input()
        print('Your answer:', user_answer)

        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was \
'{correct_answer}'.\nLet's try again, {username}!")
            return

    else:
        print(f'Congratulations, {username}!')

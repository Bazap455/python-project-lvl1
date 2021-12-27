import prompt


NUMBER_OF_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def run(game):
    username = welcome_user()
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

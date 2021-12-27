from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_progression(a1, d, length):
    progression = []

    for i in range(length):
        ai = a1 + i * d
        progression.append(str(ai))

    return progression


def generate_round():
    a1 = randint(1, 10)     # First member of progression.
    d = randint(1, 10)      # Difference of successive members
    length = randint(5, 10)
    progression = get_progression(a1, d, length)
    hidden_pos = randint(1, length)
    correct_answer = str(progression[hidden_pos - 1])
    progression[hidden_pos - 1] = '..'
    question = " ".join(progression)
    return correct_answer, question

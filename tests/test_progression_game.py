from brain_games.games.progression_game import get_progression, generate_round


def test_get_progression():
    assert get_progression(1, 2, 5) == ['1', '3', '5', '7', '9']


def test_generate_round():
    answer, question = generate_round()
    progression = question.split()
    hidden_index = progression.index('..')
    progression[hidden_index] = answer
    a1 = int(progression[0])
    d = int(progression[1]) - int(progression[0])
    length = len(progression)
    assert progression == get_progression(a1, d, length)

from brain_games.games.calc_game import generate_round


def test_generate_round():
    correct_answer, question = generate_round()
    assert eval(question) == int(correct_answer)

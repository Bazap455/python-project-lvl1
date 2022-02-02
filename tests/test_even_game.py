from brain_games.games.even_game import is_even, generate_round


def test_is_even():
    assert not is_even(-1)
    assert is_even(0)
    assert is_even(2)


def test_generate_round():
    answer, question = generate_round()

    if is_even(int(question)):
        assert answer == 'yes'
    else:
        assert answer == 'no'

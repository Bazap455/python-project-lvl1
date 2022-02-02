from brain_games.games.prime_game import is_prime, generate_round


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert not is_prime(4)


def test_generate_round():
    answer, question = generate_round()

    if is_prime(question):
        assert answer == 'yes'
    else:
        assert answer == 'no'

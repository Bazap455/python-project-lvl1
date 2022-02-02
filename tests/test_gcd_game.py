from brain_games.games.gcd_game import gcd, generate_round


def test_gcd():
    assert gcd(1, 1) == 1
    assert gcd(6, 8) == gcd(8, 6) == 2
    assert gcd(3, 17) == gcd(17, 3) == 1


def test_generate_round():
    answer, question = generate_round()
    arguments = question.split()
    a, b = int(arguments[0]), int(arguments[1])
    assert answer == str(gcd(a, b))

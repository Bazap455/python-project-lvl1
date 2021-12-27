from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):

    if b > a:
        a, b = b, a

    r = a % b

    while r:
        a, b = b, r
        r = a % b

    return b


def generate_round():
    a = randint(1, 20)
    b = randint(1, 20)
    correct_answer = gcd(a, b)
    correct_answer = str(correct_answer)
    question = str(a) + ' ' + str(b)
    return correct_answer, question

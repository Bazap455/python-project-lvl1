#!/usr/bin/env python

from brain_games import welcome_user
from brain_games.games import prime_game


def main():
    name = welcome_user.get_name()
    prime_game.main(name)


if __name__ == '__main__':
    main()

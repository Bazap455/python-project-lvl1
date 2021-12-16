#!/usr/bin/env python

from brain_games import welcome_user
from brain_games.games import even_game


def main():
    name = welcome_user.get_name()
    even_game.main(name)


if __name__ == '__main__':
    main()

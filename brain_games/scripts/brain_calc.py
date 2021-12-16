#!/usr/bin/env python

from brain_games import welcome_user
from brain_games.games import calc_game


def main():
    name = welcome_user.get_name()
    calc_game.main(name)


if __name__ == '__main__':
    main()

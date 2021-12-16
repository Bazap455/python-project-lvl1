#!/usr/bin/env python

from brain_games import welcome_user
from brain_games.games import progression_game


def main():
    name = welcome_user.get_name()
    progression_game.main(name)


if __name__ == '__main__':
    main()

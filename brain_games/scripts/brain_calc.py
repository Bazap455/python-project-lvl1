#!/usr/bin/env python

from brain_games import welcome_user, game_calc


def main():
    name = welcome_user.get_name()
    game_calc.main(name)


if __name__ == '__main__':
    main()

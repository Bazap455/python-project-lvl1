#!/usr/bin/env python

from brain_games import welcome_user, game_even


def main():
    name = welcome_user.get_name()
    game_even.main(name)


if __name__ == '__main__':
    main()

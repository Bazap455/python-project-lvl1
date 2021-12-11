#!/usr/bin/env python

from brain_games import welcome_user, games


def main():
    name = welcome_user.get_name()
    games.gcd(name)


if __name__ == '__main__':
    main()

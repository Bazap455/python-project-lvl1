#!/usr/bin/env python

import prompt


def get_username():
    '''Welcome user and return name of user.'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


if __name__ == '__main__':
    get_username()

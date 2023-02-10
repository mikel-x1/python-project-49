#!/usr/bin/env python3

from brain_games.Engine import game
from brain_games.Games.even import rule, even


def main():
    print('Welcome to the Brain Games!')
    game(rule, even)


if __name__ == '__main__':
    main()

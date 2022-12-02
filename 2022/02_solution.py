# --- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2
# code 2022-12-02

import time
simple = False
verbose = 1

if simple:
    data = 'A Y\nB X\nC Z'.splitlines()
else:
    file = open('02_input.txt', 'r')
    data = file.read().splitlines()  # strip()


def main():
    start_time = time.time()
    points = 0
    for line in data:
        points += rps(line.split(' '))
    print(f'First round points: {points}')
    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    points = 0
    for line in data:
        points += rps(decide(line.split(' ')))
    print(f'Second round points: {points}')
    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


def rps(play):
    assert play[0] in ['A', 'B', 'C'], 'invalid input player1'
    assert play[1] in ['X', 'Y', 'Z'], 'invalid input player2'
    if play[0] == 'A':    # Rock
        if play[1] == 'X':     # Rock 1
            return 1 + 3
        if play[1] == 'Y':     # Paper 2
            return 2 + 6
        return 3 + 0           # Scissor 3
    elif play[0] == 'B':  # Paper
        if play[1] == 'X':     # Rock 1
            return 1 + 0
        elif play[1] == 'Y':   # Paper 2
            return 2 + 3
        return 3 + 6           # Scissor 3
    else:                 # Scissor
        if play[1] == 'X':     # Rock 1
            return 1 + 6
        elif play[1] == 'Y':   # Paper 2
            return 2 + 0
        return 3 + 3           # Scissor 3


def decide(play):
    assert play[0] in ['A', 'B', 'C'], 'invalid input player1'
    assert play[1] in ['X', 'Y', 'Z'], 'invalid input player2'
    if play[0] == 'A':    # Rock
        if play[1] == 'X':     # Loose
            return [play[0], 'Z']
        if play[1] == 'Y':     # Draw
            return [play[0], 'X']
        return [play[0], 'Y']  # Win
    elif play[0] == 'B':  # Paper
        if play[1] == 'X':     # Loose
            return [play[0], 'X']
        if play[1] == 'Y':     # Draw
            return [play[0], 'Y']
        return [play[0], 'Z']  # Win
    else:                 # Scissor
        if play[1] == 'X':     # Loose
            return [play[0], 'Y']
        if play[1] == 'Y':     # Draw
            return [play[0], 'Z']
        return [play[0], 'X']  # Win


if __name__ == '__main__':
    main()

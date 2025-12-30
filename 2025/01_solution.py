# --- Day 1: Secret Entrance ---
# https://adventofcode.com/2025/day/1

import time
simple = True

if simple:
    data = 'L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82'.splitlines()
else:
    with open('01_input.txt', 'r', encoding='ascii') as file:
        data = file.read().splitlines()


def main():
    start_time = time.time()
    pwd = 0
    dial = 50
    for d in data:
        if d[0] == 'L':
            dial -= int(d[1:])
        elif d[0] == 'R':
            dial += int(d[1:])
        else:
            print("ERROR")
        dial %= 100
        if dial == 0:
            pwd += 1
    print(f"part 1: {pwd}")

    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    pwd = 0
    dial = 50
    for d in data:
        if d[0] == 'L':
            turn = -int(d[1:])
        elif d[0] == 'R':
            turn = int(d[1:])
        else:
            print("ERROR")
            turn = 0

        while turn > 0:
            turn -= 1
            dial += 1
            dial %= 100
            if dial == 0:
                pwd += 1
        while turn < 0:
            turn += 1
            dial -= 1
            dial %= 100
            if dial == 0:
                pwd += 1

    print(f"part 2: {pwd}")

    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

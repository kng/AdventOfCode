# --- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1
# code 2022-12-02

import time
simple = False
verbose = 1

if simple:
    data = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n'.splitlines()
else:
    file = open('01_input.txt', 'r')
    data = file.read().splitlines()  # strip()


def main():
    start_time = time.time()
    carried = []
    calories = 0

    for line in data:
        if len(line) == 0:
            carried.append(calories)
            calories = 0
        else:
            calories += int(line)
    carried.append(calories)
    print(f'Highest calories carried: {max(carried)}')
    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    carried.sort()
    print(f'Sum of top three: {sum(carried[-3:])}')
    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

# --- Day 3: Rucksack Reorganization ---
# https://adventofcode.com/2022/day/3
# code 2022-12-23

import time
simple = True

if simple:
    data = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\n' \
           'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'.splitlines()
else:
    file = open('03_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()
    both = []
    for line in data:
        c1 = set(line[:len(line)//2])
        c2 = set(line[len(line)//2:])
        both.append(next(iter(c1 & c2)))
    prio = [ord(x)-96 if x > 'Z' else ord(x)-38 for x in both]  # a-z -> 1-26, A-Z -> 27-52
    print(f'Sum of the priorities: {sum(prio)}')
    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    i = 0
    group = []
    while i < len(data) - 2:
        group.append(next(iter(set(data[i]) & set(data[i+1]) & set(data[i+2]))))
        i += 3
    prio = [ord(x)-96 if x > 'Z' else ord(x)-38 for x in group]
    print(f'Group sum: {sum(prio)}')
    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

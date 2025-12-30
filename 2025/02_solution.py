# --- Day 2: Gift Shop ---
# https://adventofcode.com/2025/day/2

import time
simple = True

if simple:
    data = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,' \
           '446443-446449,38593856-38593862,565653-565659,824824821-824824827,' \
           '2121212118-2121212124'.split(',')
else:
    with open('02_input.txt', 'r', encoding="ascii") as file:
        data = file.read().split(',')


def main():
    start_time = time.time()
    inv = 0
    for ds in data:
        d = [int(x) for x in ds.split("-")]
        assert len(d) == 2
        for i in range(d[0], d[1] + 1):
            s = str(i)
            n = len(s)
            if s[0:n//2] == s[n//2:]:
                inv += i
    print(f"part 1: {inv}")

    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    inv = 0
    for ds in data:
        d = [int(x) for x in ds.split("-")]
        assert len(d) == 2
        for i in range(d[0], d[1] + 1):
            s = str(i)
            n = len(s)
            for j in range(1, n//2+1):
                if n % j == 0:
                    t = [s[x:x + j] for x in range(0, n, j)]
                    if len(set(t)) == 1:
                        inv += i
                        break
    print(f"part 2: {inv}")

    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

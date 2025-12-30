# --- Day 3: Lobby ---
# https://adventofcode.com/2025/day/3

import time
simple = True

if simple:
    data = '987654321111111\n' \
           '811111111111119\n' \
           '234234234234278\n' \
           '818181911112111'.splitlines()
else:
    with open('03_input.txt', 'r', encoding='ascii') as file:
        data = file.read().splitlines()


def main():
    start_time = time.time()

    jolt = 0
    batt = 2
    for d in data:
        d1 = max(int(x) for x in d[0:-batt+1])
        s = d.find(str(d1))
        d2 = max(int(x) for x in d[s+1:])
        jolt += int(f"{d1}{d2}")

    print(f"part 1: {jolt}")

    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    jolt = 0
    for d in data:
        batt = 12
        p = 0
        r = []
        for i in range(batt - 1, -1, -1):
            if i == 0:
                m = max(int(x) for x in d[p:])
            else:
                m = max(int(x) for x in d[p:-i])
            p = d.find(str(m), p)
            r.append(d[p])
            p += 1
        jolt += int(''.join(r))
    print(f"part 2: {jolt}")

    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

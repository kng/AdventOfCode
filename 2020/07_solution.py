# --- Day 7: Handy Haversacks ---
# https://adventofcode.com/2020/day/7

# Second part incomplete!

import time
import re
simple = 1  # 0 = puzzle input, 1 = part one, 2 = part two
verbose = 0

if simple == 1:
    data = "light red bags contain 1 bright white bag, 2 muted yellow bags.\n" \
           "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n" \
           "bright white bags contain 1 shiny gold bag.\n" \
           "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n" \
           "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n" \
           "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n" \
           "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n" \
           "faded blue bags contain no other bags.\n" \
           "dotted black bags contain no other bags.\n".splitlines()
elif simple == 2:
    data = "shiny gold bags contain 2 dark red bags.\n" \
           "dark red bags contain 2 dark orange bags.\n" \
           "dark orange bags contain 2 dark yellow bags.\n" \
           "dark yellow bags contain 2 dark green bags.\n" \
           "dark green bags contain 2 dark blue bags.\n" \
           "dark blue bags contain 2 dark violet bags.\n" \
           "dark violet bags contain no other bags.".splitlines()
else:
    file = open('07_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    bags = re.compile(r'\d+ (\w+\s\w+) bag', re.IGNORECASE)
    rules = {}
    for row in data:
        a = row.split(' bags contain ')
        rules[a[0]] = bags.findall(a[1])
        if verbose > 2:
            print('{}'.format(row))
        if verbose > 2:
            print('{} {}'.format(a[0], rules[a[0]]))
    if verbose > 1:
        print('{}'.format(rules))

    bag = {'shiny gold'}
    holds = set()
    while bag:
        b = bag.pop()
        if verbose > 1:
            print('searching for \'{}\''.format(b))
        for k, v in rules.items():
            if b in v:
                holds |= {k}
                bag |= {k}
                if verbose > 0:
                    print('found \'{}\' holding {}'.format(k, v))

    print('it can be found in {} bags'.format(len(holds)))
    # only works with simple = 1 or 0

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    print('second part does NOT work yet!')
    bags = re.compile(r'(\d+) (\w+\s\w+) bag', re.IGNORECASE)
    rules = {}
    for row in data:
        a = row.split(' bags contain ')
        rules[a[0]] = bags.findall(a[1])
        if verbose > 2:
            print('{}'.format(row))
        if verbose > 2:
            print('{} {}'.format(a[0], rules[a[0]]))
    if verbose > 0:
        print('{}'.format(rules))

    bag = {(1, 'shiny gold')}
    stack = ''
    while bag:
        b = bag.pop()
        if verbose > 0:
            print('searching for \'{}\''.format(b[1]))
        for k, v in rules.items():
            if b[1] in k:
                stack += str(b[0]) + '*'
                bag |= set(v)
                if verbose > 0:
                    print('found \'{}\' holding {}'.format(k, v))

    print('it requires {} bags'.format(stack))
    # only works with simple = 2 or 0

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()

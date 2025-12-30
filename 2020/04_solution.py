# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4

import time
simple = True
verbose = 0

if simple:
    data = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n" \
           "byr:1937 iyr:2017 cid:147 hgt:183cm\n\n" \
           "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n" \
           "hcl:#cfa07d byr:1929\n\n" \
           "hcl:#ae17e1 iyr:2013\n" \
           "eyr:2024\n" \
           "ecl:brn pid:760753108 byr:1931\n" \
           "hgt:179cm\n\n" \
           "hcl:#cfa07d eyr:2025 pid:166559648\n" \
           "iyr:2011 ecl:brn hgt:59in".splitlines()
else:
    file = open('04_input.txt', 'r')  # make sure it ends in a blank line
    data = file.read().splitlines()


def main():
    start_time = time.time()
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'

    pp = ''
    valid = 0
    for row in data:
        if len(row) > 0:
            pp += row + ' '
        else:
            pd = [pi.split(':')[0] for pi in pp.split()]
            if verbose > 1:
                print('{}'.format(pd))
            if all(elem in pd for elem in req):
                valid += 1
            pp = ''
    print('valid: {}'.format(valid+1))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    pp = ''
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = 0
    score = 0
    for row in data:
        if len(row) > 0:
            pp += row + ' '
        else:
            pd = [pi.split(':') for pi in pp.split()]
            for pdv in pd:
                if verbose > 1:
                    print('{}'.format(pdv))
                if pdv[0] == 'byr' and 1920 <= int(pdv[1]) <= 2002:
                    score += 1
                if pdv[0] == 'iyr' and 2010 <= int(pdv[1]) <= 2020:
                    score += 1
                if pdv[0] == 'eyr' and 2020 <= int(pdv[1]) <= 2030:
                    score += 1
                if pdv[0] == 'hgt':
                    if 'cm' in pdv[1]:
                        if 150 <= int(''.join([i for i in pdv[1] if i.isdigit()])) <= 193:
                            score += 1
                    elif 'in' in pdv[1]:
                        if 59 <= int(''.join([i for i in pdv[1] if i.isdigit()])) <= 76:
                            score += 1
                if pdv[0] == 'hcl' and len(''.join(i for i in pdv[1] if i.isdigit() or i in '#abcdef')) == 7:
                    score += 1
                if pdv[0] == 'ecl' and pdv[1] in ecls:
                    score += 1
                if pdv[0] == 'pid' and len(''.join(i for i in pdv[1] if i.isdigit())) == 9:
                    score += 1
            if score >= 7:
                valid += 1
            if verbose > 0:
                print('{} {}'.format(score, pp))
            score = 0
            pp = ''
    print('valid: {}'.format(valid+1))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()

import time
simple = True
verbose = 1

if simple:
    data = '123\n456'.splitlines()
else:
    file = open('00_input.txt', 'r')
    data = file.read().splitlines()  # strip()


def main():
    start_time = time.time()

    middle_time = time.time()
    print(f'time elapsed: {middle_time - start_time}')

    end_time = time.time()
    print(f'time elapsed: {end_time - middle_time}')


if __name__ == '__main__':
    main()

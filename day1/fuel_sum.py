import math


def fuel_sum(fuel_list):
    result = 0
    for l in fuel_list:
        result += math.floor(l/3) - 2
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [int(l) for l in f.read().splitlines()]
        print(fuel_sum(lines))

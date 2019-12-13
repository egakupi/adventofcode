import math


def get_answer(fuel_list):
    sum, total = 0, 0
    for l in fuel_list:
        sum += calculate_fuel(l)
        total += calculate_total_fuel(l)
    return sum, total


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_total_fuel(mass):
    calc = calculate_fuel(mass)
    if calc <= 0:
        return 0
    return calc + calculate_total_fuel(calc)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [int(l) for l in f.read().splitlines()]
        sum_fuel, total_fuel = get_answer()
        print(f'Fuel sum: {get_answer(lines)[0]}, total fuel sum: {get_answer(lines)[1]}')

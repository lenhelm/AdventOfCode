from advent.year_2021.utils import get_data_path


def first_solution():
    data = read_input("day_7.txt")
    solution = optimize(data, calculate_costs)
    return solution


def second_solution():
    data = read_input("day_7.txt")
    solution = optimize(data, calculate_modified_costs)
    return solution


def read_input(file_name):
    with open(get_data_path() / file_name, "r") as file:
        data = file.readlines()
        return [int(x) for x in data[0].split(",")]


def optimize(input_data: list, func):
    costs = {}
    for pos in range(0, max(input_data)):
        costs[pos] = func(input_data, pos)
    min_pos, min_costs = sorted(costs.items(), key=lambda x: x[1])[0]
    return min_pos, min_costs


def calculate_costs(data: list, target_pos: int):
    return sum([abs(pos - target_pos) for pos in data])


def calculate_modified_costs(data: list, target_pos: int):
    return sum([calc_fuel(abs(pos - target_pos)) for pos in data])


def calc_fuel(steps: int):
    return 1 / 2 * steps * (steps + 1)

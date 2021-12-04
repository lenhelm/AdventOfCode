from copy import deepcopy


def create_solution_part1(input_data: list) -> dict:
    input = count_occurence(input_data)
    gamma = int(''.join([get_max_key(x) for x in input.values()]), 2)
    epsilon = int(''.join([get_min_key(x) for x in input.values()]), 2)

    return {
        'gamma': gamma,
        'epsilon': epsilon,
        'solution': gamma * epsilon
    }


def create_solution_part2(input_data: list):
    oxygen = int(evaluate(input_data, get_max_key), 2)
    co2_scrubber = int(evaluate(input_data, get_min_key), 2)

    return {
        'oxygen': oxygen,
        'co2_scrubber': co2_scrubber,
        'solution': oxygen * co2_scrubber
    }


def evaluate(input_data: list, func) -> dict:
    data = deepcopy(input_data)
    for i in range(len(data[0])):
        counts = count_occurence(data)
        number = func(counts[i])
        data = filter_binaries(data, i, number)
        if len(data) == 1:
            return data[0]


def filter_binaries(input: list, position: int, number: str) -> list:
    return [x for x in input if x[position] == number]


def count_occurence(input_data: list) -> int:
    res = {}
    for bit_string in input_data:
        for x in range(len(bit_string)):
            try:
                res[x]
            except KeyError:
                res[x] = {'1': 0, '0': 0}
            if bit_string[x] == '1':
                res[x]['1'] +=1
            else:
                res[x]['0'] += 1
    return res


def get_max_key(input: dict):
    if input['1'] >= input['0']:
        return '1'
    else:
        return '0'


def get_min_key(input: dict):
    if input['1'] < input['0']:
        return '1'
    else:
        return '0'
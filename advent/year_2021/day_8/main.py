from advent.year_2021.utils import get_data_path


def read_input(file_name: str):
    output = {}
    with open(get_data_path() / file_name, "r") as file:
        line_num = 0
        for line in file.readlines():
            output[line_num] = [x.split() for x in line.split("|")]
            line_num += 1
    return output


def first_solution():
    data = read_input("day_8.txt")
    length_patterns = [2, 3, 4, 7]
    count = 0
    for inputs in data.values():
        for input in inputs[1]:
            if len(input) in length_patterns:
                count += 1
    return count

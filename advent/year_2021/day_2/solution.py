def read_data(input_file) -> list:
    output = []
    with open(input_file, "r") as file:
        for line in file.readlines():
            command, number = line.split()
            output.append((command, int(number)))
    return output


# Part 1
def evaluate(data: list) -> set:
    depth = 0
    horizontal = 0
    for i in range(0, len(data)):
        command, number = data[i]
        if command == "forward":
            horizontal += number
        elif command == "down":
            depth += number
        else:
            depth -= number
    return depth, horizontal


# Part2
def evaluate_aim(data: list) -> set:
    depth = 0
    horizontal = 0
    aim = 0
    for i in range(0, len(data)):
        command, number = data[i]
        if command == "forward":
            horizontal += number
            depth += aim * number
        elif command == "down":
            aim += number
        else:
            aim -= number
    return depth, horizontal, depth * horizontal

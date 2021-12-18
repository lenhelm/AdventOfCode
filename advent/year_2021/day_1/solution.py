def read_data(input_file):
    output = []
    with open(input_file, "r") as file:
        for line in file.readlines():
            output.append(int(line.strip()))
    return output


def evaluate(data):
    count_increase = 0
    for i in range(1, len(data)):
        res = data[i - 1] - data[i]
        if res < 0:
            count_increase += 1
    return count_increase


def evaluate_sliding_window(data):
    count_increase = 0
    for i in range(0, len(data)):
        try:
            win1 = data[i] + data[i + 1] + data[i + 2]
            win2 = data[i + 1] + data[i + 2] + data[i + 3]
            if (win1 - win2) < 0:
                count_increase += 1
        except IndexError:
            return count_increase

def read_data(input_file):
    output = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            output.append(line.strip())
    return output

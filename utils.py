def read_data(input_file):
    output = []
    with open(input_file, 'r') as file:
        for line in file.readlines():
            output.append(line.strip())
    return output


def read_bingo_data(input_file):
    output = {}
    with open(input_file, 'r') as file:
        bingo_batch = 0
        for line in file.readlines():
            if len(line.split(',')) > 5:
                output['drawn_numbers'] = line.split(',')
            elif len(line) < 5:
                bingo_batch +=1
                output[bingo_batch] = []
            else:
                output[bingo_batch].append(line.split())
        return output

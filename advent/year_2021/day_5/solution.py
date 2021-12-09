from advent.year_2021.day_5.objects import Point, Row


def read_data(file_path):
    rows = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line_split = line.split()
            x1, y1 = [int(x) for x in line_split[0].split(',')]
            x2, y2 = [int(x) for x in line_split[2].split(',')]

            if any([x1 == x2, y1 == y2]):
                rows.append(Row(Point(x1, y1), Point(x2, y2)))
    return rows

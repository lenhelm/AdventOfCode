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


def calculate_intersections(data: list):
    found_intersections = []
    count = 0
    for line_count in range(len(data)):
        try:
            intersections = data[line_count].evaluate(data[line_count + 1])
            if intersections:
                for intersection in intersections:
                    if intersection not in found_intersections:
                        count += 1
                        #found_intersections.append(intersection)
        except IndexError:
            return count

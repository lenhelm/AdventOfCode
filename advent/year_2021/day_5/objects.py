from itertools import product


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash(f"x:{self.x};y:{self.y}")
    
    def __eq__(self, other):
        if isinstance(other, Point):
            if all([self.x == other.x, self.y == other.y]):
                return True
            return False


class Row:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.points = self.calculate_row(start, end)
    
    @staticmethod
    def calculate_row(start, end):
        x_min, x_max = sorted([start.x, end.x])
        y_min, y_max = sorted([start.y, end.y])
        x_range = range(x_min, x_max+1)
        y_range = range(y_min, y_max+1)
        return [Point(x, y) for x in x_range for y in y_range]

    def evaluate(self, row):
        hits = []
        for point in product(self.points, row.points):
            if point[0] == point[1] and point[0] not in hits:
                hits.append(point[0])
        return hits


    
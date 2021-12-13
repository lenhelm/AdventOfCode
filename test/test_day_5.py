from advent.year_2021.day_5.objects import Point, Row
from advent.year_2021.day_5.solution import calculate_intersections


def test_point():
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2


def test_point_equals():
    p1 = Point(1,1)
    p2 = Point(1,1)
    p3 = Point(2,2)
    
    assert p1 == p2
    assert p1 != p3


def test_row():
    row = Row(Point(1,1), Point(1,3))
    assert row.points == [Point(1,1), Point(1,2), Point(1,3)]


def test_row_evaluate():
    row1 = Row(Point(1,1), Point(1,3))
    row2 = Row(Point(1,2), Point(1,4))

    assert row1.evaluate(row2) == [Point(1,2), Point(1,3)]


def test_calculate_intersections():
    input = [
        Row(Point(1,2), Point(1,5)), # (1,2), (1,3), (1,4), (1,5)
        Row(Point(1,5), Point(1,10)), # (1,5), (1,6), (1,7), (1,8), (1,9), (1,10)
        Row(Point(1,5), Point(5,5)), # (1,5), (2,6), (3,7), (4,8), (5,9)
        Row(Point(1,6), Point(5,6)) # (1,6), (2,6), (3,6), (4,6), (5,6)
        ]
    expected_output = 2
    assert expected_output == calculate_intersections(input)
    
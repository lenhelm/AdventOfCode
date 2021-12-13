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
    input = [Row(Point(1,2), Point(1,3)), Row(Point(1,3), Point(1,4)), Row(Point(1,5), Point(1,9))]
    expected_output = 1
    assert expected_output == calculate_intersections(input)
    
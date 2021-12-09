from advent.year_2021.day_5.solution import Point, Row


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

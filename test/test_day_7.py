from advent.year_2021.day_7.main import first_solution, optimize, calculate_costs


def test_calculate_costs():
    input = [5, 10, 15]
    input_pos = 5
    expected = 15
    assert calculate_costs(input, input_pos) == expected


def test_optimize():
    input = [0, 5, 10, 15, 20]
    expected = (10, 30)
    assert optimize(input) == expected

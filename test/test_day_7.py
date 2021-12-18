from pathlib import Path

from advent.year_2021.day_7.main import (
    first_solution,
    optimize,
    calculate_costs,
    read_input,
)
from advent.year_2021 import utils


def test_calculate_costs():
    input = [5, 10, 15]
    input_pos = 5
    expected = 15
    assert calculate_costs(input, input_pos) == expected


def test_optimize():
    input = [0, 5, 10, 15, 20]
    expected = (10, 30)
    assert optimize(input) == expected


def test_read_input():
    data = read_input("day_7.txt")
    assert type(data) == list
    assert all([type(x) == int for x in data])

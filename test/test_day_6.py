from advent.year_2021.day_6.objects import Latenfish
from advent.year_2021.day_6.solution import create_swarm, one_day_passes, solution_part1


def test_latenfish_init():
    latenfish = Latenfish(5)
    assert latenfish.days == 5


def test_latenfish_lower_days():
    latenfish = Latenfish(5)
    latenfish.lower_days()
    assert latenfish.days == 4


def test_latenfish_reset():
    latenfish = Latenfish(0)
    latenfish.reset()
    assert latenfish.days == 6


def test_create_swarm():
    input = [1, 2, 3]
    output = create_swarm(input)
    assert isinstance(output[0], Latenfish)
    assert output[0].days == 1
    assert output[1].days == 2
    assert len(output) == 3


def test_one_day_passes():
    input = [
        Latenfish(0),
        Latenfish(0),
        Latenfish(2)
    ]
    output = one_day_passes(input)
    assert output[0].days == 6
    assert output[1].days == 6
    assert output[2].days == 1
    assert len(output) == 5


def test_solution_part1():
    input = [1,2]
    output = solution_part1(input, 2)
    expected = 3
    assert output == expected

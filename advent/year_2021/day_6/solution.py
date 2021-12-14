from advent.year_2021.day_6.objects import Latenfish


def solution_part1(data: list, days: int):
    swarm = create_swarm(data)
    for _ in range(days):
        swarm = one_day_passes(swarm)
    return len(swarm)


def create_swarm(data: list):
    return [Latenfish(x) for x in data]


def one_day_passes(swarm: list):
    new_born = 0
    for x in swarm:
        x.lower_days()
        if x.days == -1:
            new_born += 1
            x.reset()
    return swarm + [Latenfish(8) for x in range(new_born)]
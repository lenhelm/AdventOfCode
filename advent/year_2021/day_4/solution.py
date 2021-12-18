import numpy as np


def read_bingo_data(input_file):
    """Read the bingo data"""
    output = {}
    with open(input_file, "r") as file:
        bingo_batch = 0
        for line in file.readlines():
            if len(line.split(",")) > 5:
                output["drawn_numbers"] = [int(x) for x in line.split(",")]
            elif len(line) < 5:
                bingo_batch += 1
                output[bingo_batch] = []
            else:
                output[bingo_batch].append(line.split())
        return output


class Game:
    """A game with different bingo grids. Evaluate an array of drawn numbers
    and receive a dictionary with the first winning grid and the last winning
    grid."""

    def __init__(self, data: dict):
        self.grids = {key: Grid(value) for key, value in data.items()}

    def evaluate(self, drawn_numbers: list) -> dict:
        leaderboard = []
        winner_grids = []
        for number in drawn_numbers:
            for grid_id, grid in self.grids.items():
                grid.cross(number)
                if grid.eval_win() and grid_id not in winner_grids:
                    winner_grids.append(grid_id)
                    leaderboard.append(
                        {
                            "grid_id": grid_id,
                            "grid_sum": grid.sum(),
                            "number": number,
                            "solution": grid.sum() * number,
                        }
                    )
        return {
            "first_winning_grid": leaderboard[0],
            "last_winning_grid": leaderboard[-1],
        }


class Grid:
    """A grid of a bingo game"""

    def __init__(self, data: list):
        self.grid = np.array(data).astype(int)

    def cross(self, number: int):
        self.grid = np.where(self.grid == number, 0, self.grid)

    def sum(self):
        return self.grid.sum()

    def eval_win(self) -> bool:
        winning_row = self.eval_win_input(self.grid)
        winning_col = self.eval_win_input(self.grid.transpose())
        if any([winning_row, winning_col]):
            return True
        return False

    @staticmethod
    def eval_win_input(grid: np.array) -> bool:
        for x in grid:
            if x.sum() == 0:
                return True
        return False

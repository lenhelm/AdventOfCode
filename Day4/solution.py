import numpy as np


class Game:

    def __init__(self, data: dict):
        self.grids = {key: Grid(value) for key, value in data.items()}
    
    def evaluate(self, drawn_numbers: list):
        leaderboard = []
        winner_grids = []
        for number in drawn_numbers:
            for grid_id, grid in self.grids.items():
                grid.cross(number)
                if grid.eval_win() and grid_id not in winner_grids:
                    winner_grids.append(grid_id)
                    leaderboard.append({
                        'grid_id': grid_id,
                        'grid_sum': grid.sum(),
                        'number': number,
                        'solution': grid.sum() * number
                    })
        return {
            'solution_part1': leaderboard[0],
            'solution_part2': leaderboard[-1]
        }


class Grid:

    def __init__(self, data: list):
        self.grid = np.array(data).astype(int)
    
    def cross(self, number):
        self.grid = np.where(self.grid == number, 0, self.grid)

    def sum(self):
        return self.grid.sum()

    def eval_win(self):
        winning_row = self.eval_win_input(self.grid)
        winning_col = self.eval_win_input(self.grid.transpose())
        if any([winning_row, winning_col]):
            return True
        return False 

    @staticmethod
    def eval_win_input(grid: np.array):
        for x in grid:
            if x.sum() == 0:
                return True
        return False

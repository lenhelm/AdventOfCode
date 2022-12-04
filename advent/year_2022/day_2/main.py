import re

WIN = 6
DRAW = 3
LOST = 0

ROCK = 1  # Rock
PAPER = 2  # Paper
SCISSORS = 3  # Scissors

DR = DRAW + ROCK
LR = LOST + ROCK
WR = WIN + ROCK
DP = DRAW + PAPER
LP = LOST + PAPER
WP = WIN + PAPER
DS = DRAW + SCISSORS
LS = LOST + SCISSORS
WS = WIN + SCISSORS


OUTCOMES = {
    'A X': (DR, LS),
    'A Y': (WP, DR), 
    'A Z': (LS, WP),
    'B X': (LR, LR),
    'B Y': (DP, DP),
    'B Z': (WS, WS),
    'C X': (WR, LP),
    'C Y': (LP, DS),
    'C Z': (DS, WR)
}




def main(path: str):
    """Calculate solution for day 2"""
    with open(path, 'r') as file:
        text = file.read()
    patterns = count_patterns(text)
    score_1 = sum((x[1] for x in patterns))
    score_2 = sum((x[2] for x in patterns))
    return score_1, score_2


def count_patterns(text: str):
    output = []
    for key, value in OUTCOMES.items():
        counts = re.findall(key, text)
        output.append((key, len(counts) * value[0], len(counts) * value[1]))
    return output


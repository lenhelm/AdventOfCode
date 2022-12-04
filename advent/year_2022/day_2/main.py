import re

WIN = 6
DRAW = 3
LOST = 0

X = 1  # Rock
Y = 2  # Paper
Z = 3  # Scissors

OUTCOMES = {
    'A X': DRAW + X,
    'A Y': WIN + Y,
    'A Z': LOST + Z,
    'B X': LOST + X, 
    'B Y': DRAW + Y,
    'B Z': WIN + Z,
    'C X': WIN + X,
    'C Y': LOST + Y,
    'C Z': DRAW + Z
}


def main(path: str):
    """Calculate solution for day 2"""
    with open(path, 'r') as file:
        text = file.read()
    patterns = count_patterns(text)
    return sum([x[1] for x in patterns])


def count_patterns(text: str):
    output = []
    for key, value in OUTCOMES.items():
        counts = re.findall(key, text)
        output.append((key, len(counts) * value))
    return output

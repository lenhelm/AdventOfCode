import re

WIN = 6
DRAW = 3
LOST = 0

A = 1  # Rock X
B = 2  # Paper Y
C = 3  # Scissors Z

OUTCOMES = {
    'A X': DRAW + A,
    'A Y': LOST + A,
    'A Z': WIN + A,
    'B X': WIN + B,
    'B Y': DRAW + B,
    'B Z': LOST + B,
    'C X': LOST + C,
    'C Y': WIN + C,
    'C Z': DRAW + C
}


def main(path: str):
    """Calculate solution for day 2"""
    with open(path, 'r') as file:
        text = file.read()
    patterns = count_patterns(text)
    return sum([x[1] for x in patterns])


def find_pattern(text: str, pattern: str):
    count = re.findall(pattern, text)
    return count


def count_patterns(text: str):
    output = []
    for key, value in OUTCOMES.items():
        counts = find_pattern(text, key)
        output.append((key, len(counts) * value))
    return output

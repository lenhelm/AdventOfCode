from collections import Counter
import string

PRIO = dict(zip(string.ascii_letters, list(range(1, 53))))


def main(path: str):
    """Main function for solution calculation"""
    with open(path, 'r') as file:
        lines = file.readlines()
    part1_score = identify_mixed_item(lines)
    part2_score = identify_badge(lines)
    return part1_score, part2_score


def identify_mixed_item(lines):
    """Calculate prio score for individual bag"""
    final_score = 0
    for line in lines:
        split_index = int(len(line) / 2)
        c1 = Counter(line[:split_index])
        c2 = Counter(line[split_index:])
        common = c1 & c2
        final_score += PRIO[list(common.keys())[0]]
    return final_score


def identify_badge(lines):
    """Identify group badges and calcuate prio score"""
    groups = chunks(lines, 3)
    score = 0
    for group in groups:
        cts = [Counter(x.strip('\n')) for x in group]
        common = cts[0] & cts[1] & cts[2]
        score += PRIO[list(common.keys())[0]]
    return score


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

from main import main, find_pattern, count_patterns


def test_main():
    # Part 1
    expected_output = 15
    output = main('test_input.txt')
    assert expected_output == output


def test_find_patterns():
    with open('test_input.txt', 'r') as file:
        text = file.read()
    test_pattern = "A Y"
    expected_output = ['A Y']
    assert find_pattern(text, test_pattern) == expected_output


def test_count_patterns():
    with open('test_input.txt', 'r') as file:
        text = file.read()
    expected_output = [('A X', 0),('A Y', 1), ('A Z', 0), ('B X', 8),
                       ('B Y', 0), ('B Z', 0), ('C X', 0), ('C Y', 0),
                       ('C Z', 6)]
    assert expected_output == count_patterns(text)

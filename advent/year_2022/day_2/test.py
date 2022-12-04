from main import main, count_patterns


def test_main():
    # Part 1
    expected_output = 45
    output = main('test_input.txt')
    assert expected_output == output


def test_count_patterns():
    with open('test_input.txt', 'r') as file:
        text = file.read()
    expected_output = [('A X', 4),('A Y', 8), ('A Z', 3), ('B X', 1),
                       ('B Y', 5), ('B Z', 9), ('C X', 7), ('C Y', 2),
                       ('C Z', 6)]
    assert expected_output == count_patterns(text)

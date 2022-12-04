from main import main, count_patterns


def test_main():
    # Part 1
    expected_output = (56, 50)
    output = main('test_input.txt')
    assert expected_output == output


def test_count_patterns():
    with open('test_input.txt', 'r') as file:
        text = file.read()
    expected_output = [('A X', 8,6),('A Y', 8,4), ('A Z', 3,8), ('B X', 1,1),
                       ('B Y', 5,5), ('B Z', 9,9), ('C X', 14,4), ('C Y', 2,6),
                       ('C Z', 6,7)]
    assert expected_output == count_patterns(text)

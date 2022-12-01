from main import Snack, Bag, populate_expedition, read_input, main


def test_main():
    single_largest_expected = 1900
    three_largest_expected = 3900
    single_largest, three_largest = main('test_input.txt')
    assert single_largest == single_largest_expected
    assert three_largest == three_largest_expected


def test_populate_expedition():
    expected_output = 3900
    expedition = populate_expedition('test_input.txt')
    assert expedition.get_calories_supply() == expected_output


def test_snack():
    snack = Snack(calories=400)
    assert snack.calories == 400


def test_bag():
    snacks = [Snack(calories=x) for x in [100, 200, 300, 400]]
    print(sorted([x.calories for x in snacks])[-1])
    bag = Bag()
    bag.add_snacks(snacks)
    assert bag.get_calories() == 1000


def test_read_input():
    expected_output = [
        [
            Snack(calories=300),
            Snack(calories=400),
            Snack(calories=200),
            Snack(calories=100)
            ],
        [
            Snack(calories=50),
            Snack(calories=50),
            Snack(calories=900)
            ],
        [
            Snack(calories=850),
            Snack(calories=50),
            Snack(calories=1000)
            ]
        ]
    output = read_input('test_input.txt')
    assert output == expected_output


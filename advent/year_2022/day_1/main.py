from dataclasses import dataclass


@dataclass
class Snack:
    calories: int = None


class Bag:
    """A bag containing snacks"""
    def __init__(self):
        self.snacks = []

    def add_snacks(self, snacks):
        """Add multiple food items"""
        self.snacks = self.snacks + snacks
        return self

    def get_calories(self):
        """Returns the sum of all food items"""
        return sum([snack.calories for snack in self.snacks])


class Elve:
    """A Elve carrying a bag"""
    def __init__(self):
        self.bag: Bag

    def set_bag(self, bag: Bag):
        self.bag = bag
        return self

    def get_calories(self):
        return self.bag.get_calories()


class Expedition:
    """An Expedition of elves"""
    def __init__(self):
        self.members = []

    def add_elves(self, elves):
        self.members = self.members + elves

    def get_calories_supply(self):
        return sum([elve.bag.get_calories() for elve in self.members])

    def sort_elves_by_bag_size(self):
        return sorted(
            self.members,
            key=lambda x: x.get_calories(),
            reverse=True
            )


def populate_expedition(path: str):
    """Populate an expedition based on an input file"""
    all_snacks = read_input(path)
    bags = [Bag().add_snacks(snacks) for snacks in all_snacks]
    elves = [Elve().set_bag(bag) for bag in bags]
    expedition = Expedition()
    expedition.add_elves(elves)
    return expedition


def read_input(path):
    """Read and transform the input data"""
    with open(path, 'r') as file:
        text = file.read()
    batches = [
        [Snack(calories=int(x)) for x in y.strip("\n").split("\n")]
        for y in text.split("\n\n")]
    return batches


def main(path: str = "../data/day_1.txt"):
    """
    Goal is to identify the elve carrying the largest amount of calories
    and return the sum
    """
    expedition = populate_expedition(path)
    sorted_elves = expedition.sort_elves_by_bag_size()

    # Part 1
    single_largest = sorted_elves[0].get_calories()
    print(f"""
    The elve with the largest amout of calories is 
    carrying {single_largest} calories
    """)

    # Part 2
    sum_three_largest = sum([elve.get_calories() for elve in sorted_elves[:3]])
    print(f"""
    The three elves with the largest amout of calories 
     carry {sum_three_largest} calories
    """)

    return single_largest, sum_three_largest

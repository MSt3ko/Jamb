import random


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Die:
    """This is a class representing a single die."""
    def __init__(self, sides=6):
        self.sides = sides
        self.value = random.randint(1, self.sides)

    sides = 6
    value = random.randint(1, sides)

    def throw(self):
        self.value = random.randint(1, self.sides)
        print(self.value)
        return self

    def get_value(self):
        print(self.value)

    def __repr__(self):
        return str(self.value)


class Dice:
    """This is a class representing a set of dice for a game."""

    def dice_sort(self):
        self.dice = sorted(self.dice, key=lambda d: d.value)

    def __init__(self, amount=5, number=6):
        self.amount = amount
        self.dice = []
        for i in range(amount):
            self.dice.append(Die(sides=number))
        self.dice_sort()

    def get_values(self):
        print(self.dice)

    def __repr__(self):
        return str(self.dice)

    '''def keep_these(self, dice_to_keep):
        if
'''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    D6_5 = Dice()
    D6_5.get_values()

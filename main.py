import random
import pandas as pd
import numpy as np


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Die:
    """This is a class representing a single die."""

    def __init__(self, sides=6, value=0):
        """
        Initializes a dice with a given amount of sides and a value.

        If a value is not given, the die is cast and receives a random value.
        """
        self.sides = sides
        if value == 0:
            self.value = random.randint(1, self.sides)
        else:
            self.value = value

    sides = 6
    value = random.randint(1, sides)

    def throw(self):
        """Throws the die to give it a new random value between 1 and the number of sides."""
        self.value = random.randint(1, self.sides)
        print(self.value)
        return self

    def get_value(self):
        print(self.value)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class Dice:
    """This is a class representing a set of dice for a game."""

    def dice_sort(self):
        """Sorts the dice for display purposes."""
        self.dice = sorted(self.dice, key=lambda d: d.value)

    def __init__(self, amount=5, sides=6):
        """Initializes a set of dice for a game of jamb. Default 5 6-sided dice."""
        self.amount = amount
        self.dice = []
        self.sides = sides
        for i in range(amount):
            self.dice.append(Die(sides=sides))
        self.dice_sort()

    def get_values(self):
        print(self.dice)

    def __repr__(self):
        return str(self.dice)

    def throw_dice(self, kept=None):
        """Throw the dice that aren't kept."""
        new_dice = []
        for i in kept:
            self.dice.remove(i)
        try:
            n = len(kept)
        except TypeError:
            n = 0
        for i in range(self.amount - n):
            new_dice.append(Die(sides=self.sides))
        self.dice = kept + new_dice
        self.dice_sort()


class Leaflet:

    def __init__(self, amount=5, sides=6, call=True):

        # Initiate empty columns and their amount, with option to exclude call
        columns = ["down", "up", "both"]
        width = 3
        if call:
            columns.append("call")
            width += 1

        # Initiate empty rows of the leaflet
        temp = {}
        empty_row = [None for i in range(width)]
        for number in range(sides):
            temp[number+1] = empty_row
        temp["Sum1"] = empty_row
        temp["Max"] = temp["Min"] = empty_row
        temp["Sum2"] = empty_row
        lower_fields = []

        if amount == 5:
            lower_fields = ["Tris", "Skala", "Full House", "Poker", "Jamb"]
        elif amount == 4:
            lower_fields = ["Tris", "Skala", "Poker"]
        else:
            raise ValueError

        for i in lower_fields:
            temp[i] = empty_row

        temp["Sum3"] = empty_row


        self.table = pd.DataFrame.from_dict(temp, orient='index')
        self.table.columns = columns


    table = pd.DataFrame()
    amount = 5
    sides = 6

    def game_standings(self):
        print(self.table)

    def calculate_points(self):
        sums = ()



    def __repr__(self):
        return "Game with " + str(self.amount) + " dice with "+str(self.sides) + " sides. There are "\
               + str(self.table.sum().sum()) + " points here."


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    D6_5 = Dice()
    D6_5.get_values()
    leaflet = Leaflet()
    leaflet.game_standings()
    print(leaflet)
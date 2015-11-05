"""
https://projecteuler.net/problem=31

Trying to find the number of different ways to make two pounds i.e. 200 pence using only
1 pence, 2 pence, 5 pence, 10 pence, 20 pence, 50 pence, pound (100 pence) and 2 pound (200 pence) coins
"""


class Coin:
    def __init__(self, value):
        self.value = value


class OnePence(Coin):
    def __init__(self):
        Coin.__init__(self, 1)


class TwoPence(Coin):
    def __init__(self):
        Coin.__init__(self, 2)


class FivePence(Coin):
    def __init__(self):
        Coin.__init__(self, 5)


class TenPence(Coin):
    def __init__(self):
        Coin.__init__(self, 10)


class TwentyPence(Coin):
    def __init__(self):
        Coin.__init__(self, 20)


class FiftyPence(Coin):
    def __init__(self):
        Coin.__init__(self, 50)


class OnePound(Coin):
    def __init__(self):
        Coin.__init__(self, 100)


class TwoPound(Coin):
    def __init__(self):
        Coin.__init__(self, 200)


value_dict = {key: 0 for key in range(0, 201)}

one = 1
two = 2
five = 5
ten = 10
twenty = 20
fifty = 50
pound = 100
two_pound = 200

value_dict[0] = 1

coin_list = [one, two, five, ten, twenty, fifty, pound, two_pound]
for coin_value in coin_list:
    for key in value_dict:
        if key >= coin_value:
            lookup_key = key - coin_value
            value_dict[key] += value_dict[lookup_key]

print value_dict[200]



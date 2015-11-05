"""
https://projecteuler.net/problem=31

Trying to find the number of different ways to make two pounds i.e. 200 pence using only
1 pence, 2 pence, 5 pence, 10 pence, 20 pence, 50 pence, pound (100 pence) and 2 pound (200 pence) coins
"""
import time


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


class CoinTypes:
    def __init__(
            self,
            include_one_pence,
            include_two_pence,
            include_five_pence,
            include_ten_pence,
            include_twenty_pence,
            include_fifty_pence,
            include_one_pound,
            include_two_pound):
        self.coins = list()
        if include_one_pence:
            self.coins.append(OnePence())

        if include_two_pence:
            self.coins.append(TwoPence())

        if include_five_pence:
            self.coins.append(FivePence())

        if include_ten_pence:
            self.coins.append(TenPence())

        if include_twenty_pence:
            self.coins.append(TwentyPence())

        if include_fifty_pence:
            self.coins.append(FiftyPence())

        if include_one_pound:
            self.coins.append(OnePound())

        if include_two_pound:
            self.coins.append(TwoPound())


def calculate_different_combinations_of_coins_to_make_value(coin_types, value):
    value_dict = {key: 0 for key in range(0, value + 1)}
    value_dict[0] = 1

    for coin in coin_types.coins:
        for key in value_dict:
            if key >= coin.value:
                lookup_key = key - coin.value
                value_dict[key] += value_dict[lookup_key]

    return value_dict[value]


def main(coin_types, value):
    start_time = time.time()

    different_combinations = calculate_different_combinations_of_coins_to_make_value(coin_types=coin_types, value=value)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "there are {0} different ways to make {1}; execution took {2} seconds".format(different_combinations, value, execution_seconds)

coin_types = CoinTypes(True, True, True, True, True, True, True, True)
main(coin_types=coin_types, value=200)



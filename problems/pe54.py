"""
https://projecteuler.net/problem=54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

# want to create a poker hand winner calculator
# takes list of hands, returns index of winning hand

# are there cards of the same value? 2 cards, 3 cards, 4 cards?
# are there cards that have consecutive values? same suit? royal flush?
# same suit only?

from collections import Counter


class Suit:
    Hearts, Diamonds, Spades, Clubs = range(4)


class Card:

    def __init__(self, high_value, low_value, suit):
        self.high_value = high_value
        self.low_value = low_value
        self.suit = suit


class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.properties = None
        self.hand_ranking = None


class HandProperties:

    def __init__(self):
        self.same_suit = None
        self.pair_list = None
        self.three_of_a_kind = None
        self.four_of_a_kind = None
        self.consecutive_card_values = None


class Pair:

    def __init__(self, value):
        self.value = value


class ThreeOfAKindProperty:

    def __init__(self, value):
        self.value = value


class FourOfAKindProperty:

    def __init__(self, value):
        self.value = value


class ConsecutiveCardValues:

    def __init__(self, highest_value):
        self.highest_value = highest_value


class SameSuit:

    def __init__(self, suit):
        self.suit = suit


class HighCard:

    def __init__(self, value, first_kicker, second_kicker, third_kicker, fourth_kicker):
        self.value = value
        self.first_kicker = first_kicker
        self.second_kicker = second_kicker
        self.third_kicker = third_kicker
        self.fourth_kicker = fourth_kicker


class OnePair:

    def __init__(self, value, first_kicker, second_kicker, third_kicker, fourth_kicker):
        self.value = value
        self.first_kicker = first_kicker
        self.second_kicker = second_kicker
        self.third_kicker = third_kicker
        self.fourth_kicker = fourth_kicker


class TwoPair:

    def __init__(self, high_pair_value, low_pair_value, kicker):
        self.high_pair_value = high_pair_value
        self.low_pair_value = low_pair_value
        self.kicker = kicker


class ThreeOfAKindHandRanking:

    def __init__(self, value, first_kicker, second_kicker):
        self.value = value
        self.first_kicker = first_kicker
        self.second_kicker = second_kicker


class Straight:

    def __init__(self, highest_value):
        self.highest_value = highest_value


class Flush:

    def __init__(self, suit, first_kicker, second_kicker, third_kicker, fourth_kicker, fifth_kicker):
        self.suit = suit
        self.first_kicker = first_kicker
        self.second_kicker = second_kicker
        self.third_kicker = third_kicker
        self.fourth_kicker = fourth_kicker
        self.fifth_kicker = fifth_kicker


class FullHouse:

    def __init__(self, three_of_a_kind_value, pair_value):
        self.three_of_a_kind_value = three_of_a_kind_value
        self.pair_value = pair_value

class FourOfAKindHandRanking:

    def __init__(self, value, kicker):
        self.value = value
        self.kicker = kicker


class StraightFlush:

    def __init__(self, suit, highest_value):
        self.suit = suit
        self.highest_value = highest_value


def is_same_suit(hand):
    if [card.suit for card in hand.card][1:] == [card.suit for card in hand.card][:-1]:
        return SameSuit(suit=hand.cards[0].suit)
    else:
        return False


def calculate_non_distinct_card_value_sets(cards, distinct_card_values, hand_properties):
    card_counter = Counter(cards)
    for distinct_card_value in distinct_card_values:
        card_value_count = card_counter[distinct_card_value]
        if card_value_count == 2:
            hand_properties.pair_list.append(Pair(distinct_card_value))
        elif card_value_count == 3:
            hand_properties.three_of_a_kind = (ThreeOfAKindProperty(distinct_card_value))
        elif card_value_count == 4:
            hand_properties.four_of_a_kind = (FourOfAKindProperty(distinct_card_value))
        else:
            RuntimeError("unexpected card value count")


def calculate_hand_properties(hand):

    hand_properties = HandProperties()

    # check if any cards of the same value
    distinct_card_values = sorted(set([card.high_value for card in hand.cards]), reverse=True)
    if distinct_card_values.__len__() < 5:
        calculate_non_distinct_card_value_sets(hand.cards, distinct_card_values, hand_properties)
    # if distinct card values equals starting card values then no duplicate cards
    else:
        same_suit = is_same_suit(hand)
        if same_suit != False:
            hand_properties.same_suit = same_suit

        sorted_cards_by_high_value = sorted([card.high_value for card in hand.cards], reverse=True)
        is_consecutive_card_high_values = True
        for card_index in range(0, 4):
            if sorted_cards_by_high_value[card_index] - 1 != sorted_cards_by_high_value[card_index + 1]:
                is_consecutive_card_high_values = False
        if is_consecutive_card_high_values:
            hand_properties.consecutive_card_values = (ConsecutiveCardValues(highest_value=sorted_cards_by_high_value[0]))
        else:
            sorted_cards_by_low_value = sorted([card.low_value for card in hand.cards], reverse=True)
            is_consecutive_card_low_values = True
            for card_index in range(0, 4):
                if sorted_cards_by_low_value[card_index] - 1 != sorted_cards_by_low_value[card_index + 1]:
                    is_consecutive_card_low_values = False
            if is_consecutive_card_low_values:
                hand_properties.consecutive_card_values = (ConsecutiveCardValues(
                    highest_value=sorted_cards_by_low_value[0]))

    hand.properties = hand_properties


def calculate_hand_ranking(hand):
    if hand.properties.consecutive_card_values is not None and hand.properties.same_suit is not None:
        hand_ranking = StraightFlush(hand.properties.same_suit, hand.properties.consecutive_card_values.highest_value)
    elif hand.properties.four_of_a_kind is not None:
        kicker = [card.high_value for card in hand.cards if card.high_value != hand.properties.four_of_a_kind.value][0]
        hand_ranking = FourOfAKindHandRanking(hand.properties.four_of_a_kind.value, kicker)
    elif hand.properties.three_of_a_kind is not None and hand.properties.pair_list.__len__() == 1:
        hand_ranking = FullHouse(hand.properties.three_of_a_kind.value, hand.properties.pair_list[0].value)
    elif hand.properties.same_suit is not None:
        sorted_cards_by_high_value = sorted([card.high_value for card in hand.cards], reverse=True)
        hand_ranking = Flush(
            hand.properties.same_suit,
            sorted_cards_by_high_value[0],
            sorted_cards_by_high_value[1],
            sorted_cards_by_high_value[2],
            sorted_cards_by_high_value[3],
            sorted_cards_by_high_value[4]
        )
    elif hand.properties.consecutive_card_values is not None:
        sorted_cards_by_high_value = sorted([card.high_value for card in hand.cards])[0]
        highest_value = sorted_cards_by_high_value[0]
        hand_ranking = Straight(highest_value)
    elif hand.properties.three_of_a_kind is not None:
        kickers = sorted([card.high_value for card in hand.cards if card.high_value != hand.properties.three_of_a_kind.value], reverse=True)
        hand_ranking = ThreeOfAKindHandRanking(
            hand.properties.three_of_a_kind.value,
            kickers[0],
            kickers[1]
        )
    elif hand.properties.pair_list.__len__() == 2:
        kicker = [card.high_value for card in hand.cards if card.high_value != hand.properties.pair_list[0].value or card.high_value != hand.properties.pair_list[1].value][0]
        hand_ranking = TwoPair(
            hand.properties.pair_list[0].value,
            hand.properties.pair_list[1].value,
            kicker
        )
    elif hand.properties.pair_list.__len__() == 1:
        kickers = sorted([card.high_value for card in hand.cards if card.high_value != hand.properties.pair_list[0].value], reverse=True)
        hand_ranking = OnePair(
            hand.properties.pair_list[0].value,
            kickers[0],
            kickers[1],
            kickers[2],
            kickers[3]
        )
    else:
        sorted_cards_by_high_value = sorted([card.high_value for card in hand.cards], reverse=True)
        hand_ranking = HighCard(
            sorted_cards_by_high_value[0],
            sorted_cards_by_high_value[1],
            sorted_cards_by_high_value[2],
            sorted_cards_by_high_value[3],
            sorted_cards_by_high_value[4]
        )
    hand.hand_ranking = hand_ranking


def calculate_winners(hands):
    straight_flushes = [hand for hand in hands if isinstance(hand.hand_ranking, StraightFlush)]
    if straight_flushes.__len__() > 0:
        










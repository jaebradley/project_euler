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

    def __str__(self):
        return "{0} - {1} - {2} ".format(self.high_value, self.low_value, self.suit)


class Hand:

    def __init__(self, cards):
        self.cards = cards


class HandRankingCalculator:

    def __init__(self, hand):
        self.hand = hand

    def is_flush(self):
        if [card.suit for card in self.hand.cards][1:] == [card.suit for card in self.hand.cards][:-1]:
            return True
        else:
            return False

    def is_high_value_straight(self):
        sorted_cards_by_high_value = sorted([card.high_value for card in self.hand.cards], reverse=True)
        is_consecutive_card_high_values = True
        for card_index in range(0, 4):
            if sorted_cards_by_high_value[card_index] - 1 != sorted_cards_by_high_value[card_index + 1]:
                is_consecutive_card_high_values = False
        if is_consecutive_card_high_values:
            return True
        else:
            return False

    def is_low_value_straight(self):
        sorted_cards_by_low_value = sorted([card.low_value for card in self.hand.cards], reverse=True)
        is_consecutive_card_low_values = True
        for card_index in range(0, 4):
            if sorted_cards_by_low_value[card_index] - 1 != sorted_cards_by_low_value[card_index + 1]:
                is_consecutive_card_low_values = False
        if is_consecutive_card_low_values:
            return True
        else:
            return False

    def is_straight(self):
        if self.is_high_value_straight() or self.is_low_value_straight():
            return True
        else:
            return False

    def is_straight_flush(self):

        if self.is_flush() and self.is_straight():
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 4 or card_counter[card_values[0]] == 1):
            return True
        else:
            return False

    def is_full_house(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 2 and (card_counter[card_values[0]] == 3 or card_counter[card_values[0]] == 2):
            return True
        else:
            return False

    def is_three_of_a_kind(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 3 or card_counter[card_values[1]] == 3 or card_counter[distinct_card_values[2]] == 3):
            return True
        else:
            return False

    def is_two_pair(self):
        card_values = [card.high_value for card in self.hand.cards]
        distinct_card_values = list(set(card_values))
        card_counter = Counter(card_values)
        if distinct_card_values.__len__() == 3 and (card_counter[card_values[0]] == 2 or card_counter[card_values[1]] == 2 or card_counter[card_values[2]] == 2):
            return True
        else:
            return False

    def is_one_pair(self):
        distinct_card_values = list(set([card.high_value for card in self.hand.cards]))
        if distinct_card_values.__len__() == 4:
            return True
        else:
            return False

    def is_high_card(self):
        distinct_card_values = list(set([card.high_value for card in self.hand.cards]))
        if not self.is_straight() and not self.is_flush() and distinct_card_values.__len__() == 5:
            return True
        else:
            return False


class HeadsUpWinnerSelector:

    def __init__(self, handA, handB):
        self.handA_ranking_calculator = HandRankingCalculator(handA)
        self.handB_ranking_calculator = HandRankingCalculator(handB)

    def select_winning_hand(self):
        if self.handA_ranking_calculator.is_straight_flush() and not self.handB_ranking_calculator.is_straight_flush():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_straight_flush() and self.handB_ranking_calculator.is_straight_flush():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_straight_flush() and self.handB_ranking_calculator.is_straight_flush():
            handA_highest_card_value = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True)[0]
            handB_highest_card_value = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True)[0]
            if handA_highest_card_value > handB_highest_card_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_card_value < handB_highest_card_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                winning_hand = None

        elif self.handA_ranking_calculator.is_four_of_a_kind() and not self.handB_ranking_calculator.is_four_of_a_kind():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_four_of_a_kind() and self.handB_ranking_calculator.is_four_of_a_kind():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_four_of_a_kind() and self.handB_ranking_calculator.is_four_of_a_kind():
            handA_four_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_four_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_four_of_a_kind_value > handB_four_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_four_of_a_kind_value < handB_four_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_kicker = min(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
                handB_kicker = min(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
                if handA_kicker > handB_kicker:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_kicker < handB_kicker:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_full_house() and not self.handB_ranking_calculator.is_full_house():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_full_house() and self.handB_ranking_calculator.is_full_house():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_full_house() and self.handB_ranking_calculator.is_full_house():
            handA_three_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_three_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_three_of_a_kind_value > handB_three_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_three_of_a_kind_value < handB_three_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_two_of_a_kind_value = min(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
                handB_two_of_a_kind_value = min(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
                if handA_two_of_a_kind_value > handB_two_of_a_kind_value:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_two_of_a_kind_value < handB_two_of_a_kind_value:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_flush() and not self.handB_ranking_calculator.is_flush():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_flush() and self.handB_ranking_calculator.is_flush():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_flush() and self.handB_ranking_calculator.is_flush():
            sorted_handA = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            sorted_handB = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            winning_hand = None
            for card_index in range(0, 5):
                if sorted_handA[card_index] > sorted_handB[card_index]:
                    winning_hand = self.handA_ranking_calculator.hand
                    break
                elif sorted_handA[card_index] < sorted_handB[card_index]:
                    winning_hand = self.handB_ranking_calculator.hand
                    break
        elif self.handA_ranking_calculator.is_straight() and not self.handB_ranking_calculator.is_straight():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_straight() and self.handB_ranking_calculator.is_straight():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_straight() and self.handB_ranking_calculator.is_straight():
            handA_highest_card_value = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True)[0]
            handB_highest_card_value = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True)[0]
            if handA_highest_card_value > handB_highest_card_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_card_value < handB_highest_card_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                winning_hand = None
        elif self.handA_ranking_calculator.is_three_of_a_kind() and not self.handB_ranking_calculator.is_three_of_a_kind():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_three_of_a_kind() and self.handB_ranking_calculator.is_three_of_a_kind():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_three_of_a_kind() and self.handB_ranking_calculator.is_three_of_a_kind():
            handA_three_of_a_kind_value = max(set(self.handA_ranking_calculator.hand.cards), key=self.handA_ranking_calculator.hand.cards.count).high_value
            handB_three_of_a_kind_value = max(set(self.handB_ranking_calculator.hand.cards), key=self.handB_ranking_calculator.hand.cards.count).high_value
            if handA_three_of_a_kind_value > handB_three_of_a_kind_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_three_of_a_kind_value < handB_three_of_a_kind_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_sorted_remaining_values = sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards if card.high_value != handA_three_of_a_kind_value], reverse=True)
                handB_sorted_remaining_values = sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards if card.high_value != handB_three_of_a_kind_value], reverse=True)
                if handA_sorted_remaining_values[0] > handB_sorted_remaining_values[0]:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_sorted_remaining_values[0] < handB_sorted_remaining_values[0]:
                    winning_hand = self.handB_ranking_calculator.hand
                elif handA_sorted_remaining_values[1] > handB_sorted_remaining_values[1]:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_sorted_remaining_values[0] < handB_sorted_remaining_values[1]:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    winning_hand = None
        elif self.handA_ranking_calculator.is_two_pair() and not self.handB_ranking_calculator.is_two_pair():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_two_pair() and self.handB_ranking_calculator.is_two_pair():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_two_pair() and self.handB_ranking_calculator.is_two_pair():
            handA_value_counter = Counter([card.high_value for card in self.handA_ranking_calculator.hand.cards])
            handB_value_counter = Counter([card.high_value for card in self.handB_ranking_calculator.hand.cards])
            handA_most_common_values = handA_value_counter.most_common()
            handB_most_common_values = handB_value_counter.most_common()
            handA_highest_pair_value = max(handA_most_common_values[0][0], handA_most_common_values[1][0])
            handA_lowest_pair_value = min(handA_most_common_values[0][0], handA_most_common_values[1][0])
            handA_kicker_value = handA_most_common_values[2][0]
            handB_highest_pair_value = max(handB_most_common_values[0][0], handB_most_common_values[1][0])
            handB_lowest_pair_value = min(handB_most_common_values[0][0], handB_most_common_values[1][0])
            handB_kicker_value = handB_most_common_values[2][0]
            if handA_highest_pair_value > handB_highest_pair_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_highest_pair_value < handB_highest_pair_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                if handA_lowest_pair_value > handB_lowest_pair_value:
                    winning_hand = self.handA_ranking_calculator.hand
                elif handA_lowest_pair_value < handB_lowest_pair_value:
                    winning_hand = self.handB_ranking_calculator.hand
                else:
                    if handA_kicker_value > handB_kicker_value:
                        winning_hand = self.handA_ranking_calculator.hand
                    elif handA_kicker_value < handB_kicker_value:
                        winning_hand = self.handB_ranking_calculator.hand
                    else:
                        winning_hand = None
        elif self.handA_ranking_calculator.is_one_pair() and not self.handB_ranking_calculator.is_one_pair():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_one_pair() and self.handB_ranking_calculator.is_one_pair():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_one_pair() and self.handB_ranking_calculator.is_one_pair():
            handA_value_counter = Counter([card.high_value for card in self.handA_ranking_calculator.hand.cards])
            handB_value_counter = Counter([card.high_value for card in self.handB_ranking_calculator.hand.cards])
            handA_most_common_value = handA_value_counter.most_common(1)[0][0]
            handB_most_common_value = handB_value_counter.most_common(1)[0][0]
            if handA_most_common_value > handB_most_common_value:
                winning_hand = self.handA_ranking_calculator.hand
            elif handA_most_common_value < handB_most_common_value:
                winning_hand = self.handB_ranking_calculator.hand
            else:
                handA_sorted_remaining_values = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards if card.high_value != handA_most_common_value], reverse=True))
                handB_sorted_remaining_values = list(sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards if card.high_value != handB_most_common_value], reverse=True))
                winning_hand = None
                for card_index in range(0, 3):
                    if handA_sorted_remaining_values[card_index] > handB_sorted_remaining_values[card_index]:
                        winning_hand = self.handA_ranking_calculator.hand
                        break
                    elif handA_sorted_remaining_values[card_index] < handB_sorted_remaining_values[card_index]:
                        winning_hand = self.handB_ranking_calculator.hand
                        break
        elif self.handA_ranking_calculator.is_high_card() and not self.handB_ranking_calculator.is_high_card():
            winning_hand = self.handA_ranking_calculator.hand
        elif not self.handA_ranking_calculator.is_high_card() and self.handB_ranking_calculator.is_high_card():
            winning_hand = self.handB_ranking_calculator.hand
        elif self.handA_ranking_calculator.is_high_card() and self.handB_ranking_calculator.is_high_card():
            handA_sorted_values = list(sorted([card.high_value for card in self.handA_ranking_calculator.hand.cards], reverse=True))
            handB_sorted_values = list(sorted([card.high_value for card in self.handB_ranking_calculator.hand.cards], reverse=True))
            winning_hand = None
            for card_index in range(0, 5):
                if handA_sorted_values[card_index] > handB_sorted_values[card_index]:
                    winning_hand = self.handA_ranking_calculator.hand
                    break
                elif handA_sorted_values[card_index] < handB_sorted_values[card_index]:
                    winning_hand = self.handB_ranking_calculator.hand
                    break
        else:
            winning_hand = None
        return winning_hand

handA = Hand(
    [Card(13, 1, 1), Card(13, 1, 2), Card(13, 1, 3), Card(13, 1, 4), Card(5, 5, 1)]
)

handB = Hand(
    [Card(13, 1, 1), Card(13, 1, 2), Card(13, 1, 3), Card(13, 1, 4), Card(5, 5, 1)]
)

heads_up_winner = HeadsUpWinnerSelector(handA, handB)
print heads_up_winner.select_winning_hand()






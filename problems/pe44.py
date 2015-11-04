"""
Find the pair of pentagonal numbers for which their sum and difference are pentagonal
"""
import time


def is_pentagonal(number):
    #inverse function for pentagonal number
    return not (1 + (1 + 24 * number) ** 0.5)/6 % 1


def return_pentagonal(n):
    return n * (3 * n - 1) / 2


def is_sum_and_difference_of_two_pentagonal_numbers_pentagonal(pentagonal1, pentagonal2):
    if is_pentagonal(pentagonal1 + pentagonal2) and is_pentagonal(abs(pentagonal1 - pentagonal2)):
        return True
    else:
        return False


def return_first_pentagonal_number_pentagonal_difference():
    found_pentagonal = False
    pentagonals = list()
    n = 1
    while not found_pentagonal:
        next_pentagonal = return_pentagonal(n=n)
        for previous_pentagonal in pentagonals:
            if is_sum_and_difference_of_two_pentagonal_numbers_pentagonal(pentagonal1=next_pentagonal, pentagonal2=previous_pentagonal):
                return next_pentagonal, previous_pentagonal
        pentagonals.append(next_pentagonal)
        n += 1


def main():
    start_time = time.time()

    pentagonal_number_1, pentagonal_number_2 = return_first_pentagonal_number_pentagonal_difference()

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "pentagonal pair is {0}, {1}; execution took {2} seconds".format(pentagonal_number_1, pentagonal_number_2, execution_seconds)

main()




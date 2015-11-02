"""
Want to find all numbers for m * n = z where concat(m, n, z) uses all digits from 1-9 exactly once
Only 2 ways to get this: either m is a 1 digit number and n is a 4 digit number OR m is a 2 digit number and n is a 3 digit number
So iterate through all possible m and n and check if concat(m, n, z) is pandigital
Return the sum of all valid pandigital identities
"""

import time


def return_number_digit_list(number):
    digit_list = []
    while number:
        digit = number % 10
        digit_list = [digit] + digit_list
        number /= 10
    return digit_list


def is_pandigital(number):
    digit_list = return_number_digit_list(number)

    if max(digit_list) != 9:
        return False

    if min(digit_list) != 1:
        return False

    sorted_digit_list = sorted(digit_list)
    index_counter = 0
    for sorted_digit in sorted_digit_list:
        if sorted_digit != index_counter + 1:
            return False
        else:
            index_counter += 1

    return True


def return_pandigital_list_for_range(start_range_m, end_range_m, start_range_n, end_range_n):
    pandigital_candidate_list = list()
    for m in range(start_range_m,end_range_m + 1):
        for n in range(start_range_n,end_range_n + 1):
            product = m * n
            number = int(str(m) + str(n) + str(product))
            if is_pandigital(number):
                pandigital_candidate_list.append(product)
    return pandigital_candidate_list


def return_pandigital_sum():
    pandigital_candidate_list = list()
    pandigital_candidate_list.extend(return_pandigital_list_for_range(0, 9, 1000, 9999))
    pandigital_candidate_list.extend(return_pandigital_list_for_range(10, 99, 100, 999))
    return sum(set(pandigital_candidate_list))


def main():
    start_time = time.time()

    pandigital_sum = return_pandigital_sum()

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "sum of all pandigital multiplicand/multiplier/product identities is {0}; execution took {1} seconds".format(pandigital_sum, execution_seconds)

main()






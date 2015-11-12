'''
Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''
from utils.project_euler_helpers import getDigits
import time


def return_last_n_digits_of_power_series_sum_to_k_inclusive(n, k):

    if k <= 0:
        raise ValueError("cannot sum to {0} because it is less than 1".format(k))

    power_series_sum = 0
    for power in range(1, k):
        power_series_sum += power ** power

    power_series_sum_digits = getDigits(number=power_series_sum)
    if n > len(power_series_sum_digits):
        raise ValueError("cannot return last {0} digits because sum is {1} digits".format(n, len(power_series_sum_digits)))

    if n <= 0:
        raise ValueError("cannot return last {0} digits because input is less than 0".format(n))

    return power_series_sum_digits[-n:]


def main(n, k):
    start_time = time.time()

    last_n_digits = return_last_n_digits_of_power_series_sum_to_k_inclusive(n=n, k=k)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "last {0} digits for power series sum to {1} are {2}; took {3} seconds".format(n, k, last_n_digits, execution_seconds)


main(10, 1000)



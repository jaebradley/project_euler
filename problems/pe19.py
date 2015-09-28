"""
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

#pretty much cheating here, but whatever
import datetime
import time


def sunday_count_for_day_of_month_in_year_range(day_of_month, start_year_inclusive, end_year_inclusive):
    count = 0
    for month in range(1, 13):
        for year in range(start_year_inclusive, end_year_inclusive + 1):
            if (datetime.datetime.strptime(str(month) + '/{0}/'.format(day_of_month) + str(year), '%m/%d/%Y').strftime('%A')) == 'Sunday':
                count += 1
    return count


def main(day_of_month, start_year_inclusive, end_year_inclusive):
    start_time = time.time()

    sunday_count = sunday_count_for_day_of_month_in_year_range(day_of_month, start_year_inclusive, end_year_inclusive)

    end_time = time.time()
    execution_seconds = end_time - start_time

    print "{0} Sundays on the {1} of the month from {2} to {3}; executed in {4} seconds".format(sunday_count, day_of_month, start_year_inclusive, end_year_inclusive, execution_seconds)

main(1, 1901, 2000)

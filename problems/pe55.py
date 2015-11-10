"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either
    (i) become a palindrome in less than fifty iterations, or,
    (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

Brute Force Solution:

1.  Iterate from 1 to 9999.
2.  Then for each number iterate the "sum a number and it's reverse" process 50 times.
3.  If the sum from step 2 is a palindrome, increment the current palindrome count by 1 and break out of the inner "50" loop.
4.  The final sum is the count of all numbers 1 to 9999 that were able to become palindromes so the answer to the problem is
    9999 - the final sum.
"""

from utils import project_euler_helpers as pe
import time

start_time = time.time()
palindrome_count = 0
for i in range(1,10000):
    old_number = i
    for count in range(0,50):
        num_string = str(old_number)
        reverse_num_string = pe.reverse_string(num_string)
        number = old_number + int(reverse_num_string)
        if pe.is_palindrome(number):
            palindrome_count += 1
            break
        else:
            old_number = number
answer = 9999 - palindrome_count
end_time = time.time()
run_time = end_time - start_time
print "Took %s seconds to run. Answer is %s." % (run_time, answer)


def return_number_and_reverse_number_sum(number):
    number_string = str(number)
    reverse_number_string = pe.reverse_string(number_string)
    return number + int(reverse_number_string)


def is_lychrel(number):
    counter = 0
    lychrel_candidate = number
    while counter < 50 and not pe.is_palindrome(lychrel_candidate):
        lychrel_candidate = return_number_and_reverse_number_sum(lychrel_candidate)
        counter += 1

    if 50 == counter and not pe.is_palindrome(lychrel_candidate):
        return True
    else:
        return False


def return_lychrel_number_count_below_limit_inclusive(limit_inclusive):
    lychrel_number_count = 0
    for candidate in range(1, limit_inclusive + 1):
        if is_lychrel(number=candidate):
            lychrel_number_count += 1
    return lychrel_number_count


def main(limit_inclusive):
    start_time = time.time()

    lychrel_number_count = return_lychrel_number_count_below_limit_inclusive(limit_inclusive=limit_inclusive)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "number of lychrel numbers under {0} inclusive is {1}; took {2} seconds".format(
        limit_inclusive,
        lychrel_number_count,
        execution_seconds
    )

main(limit_inclusive=9999)

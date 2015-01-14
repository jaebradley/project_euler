__author__ = 'jaebradley'
'''
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

Brute Force Solution:

1.  Iterate from 1 to 9999.
2.  Then for each number iterate the "sum a number and it's reverse" process 50 times.
3.  If the sum from step 2 is a palindrome, increment the current palindrome count by 1 and break out of the inner "50" loop.
4.  The final sum is the count of all numbers 1 to 9999 that were able to become palindromes so the answer to the problem is
    9999 - the final sum.
'''

import project_euler_helpers as pe
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

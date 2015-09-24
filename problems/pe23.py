"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Brute Force:

1. Iterate from 1 to 28123
2. For each number find divisors (if too slow could try caching this step in dictionary)
3. If sum of divisors > than number then log into abundant number list
4. Iterate through every tuple in abundant number list where the tuple sum < 28123 and log into list
5. Iterate from 1 to 28213 and check if number is in tuple list
"""
import math as math
num_list = [x for x in range(1,28124)]
def is_abundant(x):
    div_list = list()
    sqrt = int(math.sqrt(x)) + 1
    for i in range(1,sqrt):
        #for divisor from 1 to integer less than sqrt(x)
        if x % i is 0:
            div_list.append(i)
            if x/i != x:
                div_list.append(x/i)
    div_list.sort()
    dist_div_list = list()
    for a in range(0,len(div_list)):
        if a < len(div_list) - 1 and div_list[a] != div_list[a+1] :
            dist_div_list.append(div_list[a])
        elif a == len(div_list) - 1 and div_list[a] != div_list[a-1]:
            dist_div_list.append(div_list[a])
    if sum(dist_div_list) > x:
        return x


def abundant_list(limit):
    abundant_list = list()
    for i in range(1,limit + 1):
        print i
        output = is_abundant(i)
        if output is not None:
            abundant_list.append(output)
    return abundant_list

def abundant_tuple(mylist):
    length = len(mylist)
    abundant_tuple_list = list()
    for i in range(0,length):
        for j in range(i,length):
            tuple = mylist[i] + mylist[j]
            if tuple <= 28123:
                abundant_tuple_list.append(tuple)
            else:
                break
    abundant_tuple_list.sort()
    dist_abundant_tuple_list = list()
    abun_tup_length = len(abundant_tuple_list)
    for a in range(0,abun_tup_length):
        if a < abun_tup_length - 1 and abundant_tuple_list[a] != abundant_tuple_list[a+1] :
            dist_abundant_tuple_list.append(abundant_tuple_list[a])
        elif a == abun_tup_length - 1 and abundant_tuple_list[a] != abundant_tuple_list[a-1]:
            dist_abundant_tuple_list.append(abundant_tuple_list[a])
    return dist_abundant_tuple_list



mylist = abundant_list(28123)
print mylist
dist_abundant_tuple_list = abundant_tuple(mylist)
print sum(x for x in range(0,28124)) - sum(dist_abundant_tuple_list)



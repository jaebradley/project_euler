__author__ = 'jaebradley'
'''
base_two_list = []
word = ""
for i in range(1, 1000001):
    str_i = str(i)
    for letter in str_i:
        word += letter

    while i  > 0:
        number, multiplier = 0, 1
        number += i % 2 * multiplier
        multiplier *= 10
        number = number // 2
'''

def is_palindrome(i):
    str_i = str(i)
    word = ""
    if len(str_i) >= 1:
        for z in range(len(str_i) - 1, -1, -1):
            for letter in str_i[z]:
                word += letter
        if int(word) == i:
            return 1

def base_two(n):
    number, multiplier = 0, 1
    while n > 0:
        number += n % 2 * multiplier
        multiplier *= 10
        n = n/2
    return number


def double_palindrome():
    num_list = []
    for i in range(1,1000001):
        if (is_palindrome(base_two(i)) == 1) and (is_palindrome(i) == 1):
            num_list.append(i)
            print i, base_two(i)
    return sum(num_list)

double_palindrome_sum = double_palindrome()

__author__ = 'jaebradley'

'''
Problem:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

Strategy:

1. Build string by starting with '1' and then adding consecutive integers until the string length (1,000,000) is met.
2. After concatenating integer, I check to see if the current string is greater than the string length --
    adding the next integer might make the string go from a length of 999,998 to a length of 1,000,002.
3. If this is the case, I simply get the first one million characters of the string.
4. For any given character position in the string, return the integer equivalent so that we can use them to multiply their values.
'''

def stringBuilder():

    append_number = 1
    number_string = '1'
    max_string_length = 1000000

    while len(number_string) < max_string_length:
        append_number += 1
        append_number_string = str(append_number)
        number_string += append_number_string
        if len(number_string) > max_string_length:
            return number_string[:max_string_length]

def nthIntGetter (n,string):
    return int(string[n - 1])

string = stringBuilder()
d1 = nthIntGetter(1, string)
d10 = nthIntGetter(10, string)
d100 = nthIntGetter(100, string)
d1000 = nthIntGetter(1000, string)
d10000 = nthIntGetter(10000, string)
d100000 = nthIntGetter(100000, string)
d1000000 = nthIntGetter(1000000, string)
value = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
print value, d1, d10, d100, d1000, d10000, d100000, d1000000
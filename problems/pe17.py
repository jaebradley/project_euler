'''
if the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

1-9:
one, two, three, four, five, six, seven, eight, nine => 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 = 36

10 - 19:
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen => 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 = 70

20 - 99
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety => 6, 6, 5, 5, 5, 7, 6, 6

10 * 6 + 36 => all twenties
so  8 * 36 + 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) = 288 + 460 = 748

TOTAL FROM 1-99 = 36 + 70 + 748 = 854

100 - 999
one hundred, two hundred, etc => 10, 10, 12, 11, 11, 10, 12, 12, 11

100 * 10 + 854 + 3 * 99 = all one hundreds

100 * (10 + 10 + 12 + 11 + 11 + 10 + 12 + 12 + 11) + 9 * 854 + 3 * 99 * 9 = 9900 + 7686 + 2673 = 20259

1000

one thousand => 11

TOTAL FROM 1-1000
854 + 20259 + 11 = 21124

'''


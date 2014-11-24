__author__ = 'jaebradley'

'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. T

he lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
#basic strategy: there are 9! permutations for the first digit. First choice is 0, then 1, etc.  
#if specified number is > 9! then we know that the first choice is not 0 but 1.  Thus, we can infer which numbers the first digit is.
#for example, 2 * 9! < 1 million but 3 * 9! > 1 million, thus we know that the first digit must be list[2] or 2.
#next, we know that the remainder i.e. 1 million - 2 * 9! has 8 options or 8!, so we do the same thing.


import math

def lex(number):
    mylist=range(0,10)
    num_string=""
    rem_nums=""
    for i in range(9,0,-1):
        if number<0:
            index=0
        else:
            index=number/math.factorial(i)
        new_index=int(math.floor(index))
        print new_index
        num_string+=str(mylist[new_index])
        mylist.remove(mylist[new_index])
        print mylist
        factorial_diff=new_index * math.factorial(i)
        number=number-factorial_diff
    for z in mylist:
        rem_nums+=str(z)
    num_string+=rem_nums
    return num_string

print lex(999999) #for some reason code is returning n-1th lexicographic permutation. so first permutation is lex(0)
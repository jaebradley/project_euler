'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

1. For all numbers < 10000 (since it has 5 digits) find the string concatenation of the individual products of 1 * number, 2 * number, 3 * number, etc.
2. If numbers contain more than 9 digits, move on.
3. If numbers contain more than 1 of any digit, move on.
4. If not, then see if number is greater than current pandigital number and store original number and n if so, else do not store
'''
pandigital_list = list([0,0])
for i in range(1,10000):
    print i
    string = ''
    for mult in range(1,10000):
        string += str(i * mult).lstrip('0')
        if len(string) > 9 or string.__contains__('0'):
            break
        num_list = list()
        for a in range(0,len(string)):
            if string[a] in num_list:
                repeat = 1
                break
            elif string[a] not in num_list:
                num_list.append(string[a])
                repeat = 0
        if repeat == 0 and len(string) == 9 and int(string) > pandigital_list[1]:
            pandigital_list = list([i,int(string)])

print pandigital_list

'''
Additional Notes from mathblog.dk

First of all the fixed number must contain less than 5 digits, since n has to be greater than 1.

Second thing to not in our analysis is that we are given a candidate which starts with 9, so the fixed number we need to find needs to start with 9 as well which gives us some properties to use in the analysis.

If the fixed number is 2 digit we wont be able to generate a 9 digit number since n = 3 yields an 8 digit number and n=4 yields an 11 digit number. Same goes for 3 digit numbers where we end at 7 or 11 digits in the result. That leaves us with a four digit number starting with 9.

So already now we can limit the search to numbers between 9123 and 9876 a mere 753 numbers.

We can rather easily limit it a bit more. If the second digit is >4 then we get a carry over which results in the multiplying by 2 part will yield 19xxx instead of 18xxx and thus we have two 9’s which are not possible solutions. Further more non of the digits can be 1 since we will end up with a solution candidate with two 1’s in it.

So the solution space can be shrunk to numbers between 9234 and 9487 which means we would need to check 253 solutions.
'''




'''
Find the pair of pentagonal numbers for which their sum and difference are pentagonal
'''

def is_pentagonal(number):
    return not (1 + (1 + 24 * number) ** 0.5)/6 % 1 #inverse function for pentagonal number

def pentagonal_list(number):
    pentagonal_list = list()
    for a in range(1,number + 1):
        pentagonal = a * (3 * a - 1) / 2
        pentagonal_list.append(pentagonal)
    return pentagonal_list

pentagonal_list = pentagonal_list(3000)
for a in range(0,len(pentagonal_list) - 1):
    for b in range(a + 1,len(pentagonal_list)):
        first_pentagonal = pentagonal_list[a]
        second_pentagonal = pentagonal_list[b]
        pentagonal_sum = first_pentagonal + second_pentagonal
        pentagonal_diff = second_pentagonal - first_pentagonal
        if is_pentagonal(pentagonal_sum) and is_pentagonal(pentagonal_diff):
            print first_pentagonal,second_pentagonal,pentagonal_diff



'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Brute Force:
Notice that the first number in the spiral is at index = 0, then the next is at index = 2, and the next at index = 4.
In fact, here are the indices of the first 4 levels of the spiral:

L0 = 0
L1 = 2, 4, 6, 8
L2 = 12, 16, 20, 24
L3 = 30, 36, 42, 48

See a pattern?
L1 has a difference of 2, L2 has a difference of 4, L2 has a difference of 6, etc.
And each level has exactly 4 elements.
So basically, you increment the difference by 2 every single level
'''

total = 0
last_increment = 0
last_position = 0
position_list = list() #position indices for diagonal numbers
position_list.append(0) #adding starting index of 0 to position list
diag_list = list() #list of all our diagonal numbers
numbers = 1001 ** 2 #the square is 1001 x 1001 so it must have this many numbers

#while we have less than 1001 x 1001 numbers increase the increment by two and find the next four numbers from the last position
while total <= numbers:
    increment = last_increment + 2
    counter = 0
    while counter <= 3:
        position = last_position + increment
        last_position = position
        total = last_position
        if last_position > numbers:
            break
        position_list.append(position)
        counter += 1
    last_increment = increment

grid_list = list(x for x in range(1,numbers + 1))

for i in range(0, len(position_list)):
    print position_list[i]
    diag_list.append(grid_list[position_list[i]])

print sum(diag_list)
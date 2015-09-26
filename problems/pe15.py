"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

"""
Let's break down the 2 X 2 case:

Starting Down

D-D-R-R
D-R-D-R
D-R-R-D

Starting Right

R-D-D-R
R-D-R-D
R-R-D-D

Notice a couple things:

1. There are just as many Downs as Rights.
This makes sense since the grid is 2 x 2 and in order to get from one end of the grid to the other you at some point have to go down 2 and right 2.

2. Because of #1 there are 4 potential moves (because at some point you have to move 2D and 2R).
Another way to think about this is the following: of those 4 moves how many different ways can you choose going down twice and right twice?

This is a common combinatorial problem: N choose K.
In this case it is 4 choose 2.
N choose K is commonly solved using the formula N!/((N-K)! * K!).
In this case 4!/(2! * 2!) = 4 * 3 * 2 * 1 / 2 * 1 * 2 * 1 = 3 * 2 = 6

So to solve for 20 x 20 we just expand this principle.
Instead of 4 potential moves like before, now there are 40 (20 + 20) potential moves.
Since there must be 20 Down moves and 20 Right moves we are now solving 40 choose 20
  OR
40!/(20! * 20!) = 137846528820 (for those of you that can't do it in your head)
"""



'''
Find the next triangle number that is also pentagonal and hexagonal

triangle number = n * (n + 1) / 2
pentagonal number = n * (3n - 1) / 2
hexagonal number = n * (2n - 1) /2
'''

def is_triangle(number):
    return not (-1 +(1 + 8 * number) ** 0.5)/2 % 1 #inverse function for triangular number

def is_pentagonal(number):
    return not (1 + (1 + 24 * number) ** 0.5)/6 % 1 #inverse function for pentagonal number

for a in range(144,100000):
    hexagonal = a * (2 * a - 1)
    if is_triangle(hexagonal) == 1:
        if is_pentagonal(hexagonal) == 1:
            print hexagonal
            break



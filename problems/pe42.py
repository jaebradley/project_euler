# coding=utf-8
"""
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from utils.utilities import is_triangular
import csv
import string
import time


def return_word_value(word):
    alphabet_values = dict(zip(string.ascii_lowercase, range(1, 27)))
    word_value = 0
    for letter in word:
        word_value += alphabet_values[letter.lower()]
    return word_value


def return_triangular_word_count_in_file(csv_file_path):
    triangular_words_count = 0
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for word in row:
                if is_triangular(return_word_value(word=word)):
                    triangular_words_count += 1
    return triangular_words_count


def main(csv_file_path):
    start_time = time.time()

    triangular_word_count = return_triangular_word_count_in_file(csv_file_path=csv_file_path)

    end_time = time.time()
    execution_seconds = end_time - start_time
    print "There are {0} triangular words in {1} file; took {2} seconds".format(
        triangular_word_count, csv_file_path, execution_seconds
    )


main(csv_file_path="../static/pe42_words.txt")

# coding=utf-8
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text names_file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name rank_score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a rank_score of 938 × 53 = 49714.

What is the total of all the name scores in the names_file?
"""

import string
import time


def return_name_letter_score(name):

    #get a dictionary of letters and alphabetic-rank values
    alphabet_values = dict(zip(string.ascii_uppercase, range(1, 27)))
    #for each name, iterate through each letter and get it's alphabet rank score
    name_letter_score = 0
    for name_letter_index in range(0, len(name)):
        letter = name[name_letter_index]
        alphabet_index_value = alphabet_values[letter]
        name_letter_score += alphabet_index_value
    return name_letter_score


def name_score_calculator(names_file_path):
    #read list of names
    names_file = open(names_file_path).read().split(',')
    #sort alphabetically
    names_file.sort()
    final_score = 0
    # iterate through each name
    for name_string_index in range(0, len(names_file)):
        name = names_file[name_string_index].strip('"')
        name_letter_score = return_name_letter_score(name=name)
        #add the product of the name's alphabetic index with it's letter score
        final_score += (name_string_index + 1) * name_letter_score
    return final_score


def main(names_file_path):
    start_time = time.time()
    name_score_total = name_score_calculator(names_file_path=names_file_path)
    end_time = time.time()
    execution_seconds = end_time - start_time
    print "total name score is {0}; execution took {1} seconds".format(name_score_total, execution_seconds)


main("../static/pe22_names.txt")

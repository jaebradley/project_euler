__author__ = 'jaebradley'

import string

def create_letter_value_map():
    letter_value_map = {}
    alphabet = string.uppercase
    for i in range(0,len(alphabet)):
        letter_value_map[alphabet[i]] = i + 1
    return letter_value_map

def is_triangle(number):
    return not (-1 +(1 + 8 * number) ** 0.5)/2 % 1
    #inverse function for triangular number

def cleanAndReturnTextFile(filepath):
    raw_text = open(filepath).read().replace('"','')
    text = raw_text.split(',')
    return text

def getWordScore(word,letter_value_map):
    word_score = 0
    for i in range(0,len(word)):
        letter = word[i]
        word_score += letter_value_map[letter]
    return word_score

def findTriangularWords(text,letter_value_map):
    triangular_words = []
    for i in range(0,len(text)):
        word = text[i]
        word_score = getWordScore(word,letter_value_map)
        if is_triangle(word_score):
            triangular_words.append(word)
    return triangular_words

letter_value_map = create_letter_value_map()
text = cleanAndReturnTextFile('pe42_words.txt')
triangular_words = findTriangularWords(text,letter_value_map)
print "THERE ARE %s TRIANGULAR WORDS" % (len(triangular_words))

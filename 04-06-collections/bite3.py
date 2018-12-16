import os
import urllib.request
import pathlib

URL = 'http://bit.ly/2iQ3dlZ'
DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'tmp')
DICTIONARY = os.path.join(DIRECTORY, 'dictionary.txt')

pathlib.Path(DIRECTORY).mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(URL, DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letters: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        return [word for word in f.read().split()]


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
#     value = 0
#     for letter in word.lower():
#         for letters, score in LETTER_SCORES.items():
#             if letter in letters.lower():
#                 value += score
#     return value
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    return max(words, key=calc_word_value)


print(max_word_value(('bob', 'julian', 'pybites', 'quit', 'barbeque')))
# print(max_word_value(load_words()[20000:21000]))

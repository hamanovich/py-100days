import itertools
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
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        return [word for word in f.read().split()]


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    value = 0
    for letter in word.lower():
        for letters, score in LETTER_SCORES.items():
            if letter in letters.lower():
                value += score
    return value


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
#     full = [word for word in _get_permutations_draw(draw) if word in load_words()]
#     return list(full)
    permutations = [''.join(word).lower()
                    for word in _get_permutations_draw(draw)]
    return set(permutations) & set(load_words())



def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    # return (''.join(d).lower() for i in range(2, len(draw) + 1) for d in itertools.permutations(draw, i))
    for i in range(1, len(draw) + 1):
        yield from itertools.permutations(draw, i)


if __name__ == "__main__":
    list_of_words = get_possible_dict_words(
        ['E', 'P', 'A', 'E', 'I', 'O', 'A'])
    print(max_word_value(list_of_words))

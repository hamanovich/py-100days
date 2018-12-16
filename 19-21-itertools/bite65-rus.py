import itertools
import os

DICTIONARY = os.path.join(os.path.dirname(__file__), '..', 'tmp', 'rus.txt')

scrabble_scores = [
    (1, "А Е И Н О"),
    (2, "В Д Й К Л М П Р С Т"),
    (3, "Б Г Я"),
    (5, "Ж Ы Ь "),
    (10, "Ф Ц Ш Щ Ъ Э Ю")
]

LETTER_SCORES = {
    letter: score for score,
    letters in scrabble_scores
    for letter in letters.split()
}


def load_words():
    with open(DICTIONARY, encoding="utf8") as f:
        return [word for word in f.read().split()]


def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def get_possible_dict_words(draw):
    all_words = load_words()
    permutations = [''.join(word).lower()
                    for word in _get_permutations_draw(draw)]
    return set(permutations) & set(all_words)


def _get_permutations_draw(draw):
    for i in range(1, len(draw) + 1):
        yield from itertools.permutations(draw, i)


if __name__ == "__main__":
    list_of_words = get_possible_dict_words(list('аскма'))
    print(max_word_value(list_of_words))

from data import DICTIONARY
from data import LETTER_SCORES

def load_words():
    """Load DICTIONARY file contents into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        content = file.readlines()
        wordlist = [line.strip() for line in content]

    return wordlist


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    letters = list(word.upper())
    for i in letters:
        value += LETTER_SCORES[i]

    return value
    

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass


if __name__ == "__main__":
    calc_word_value("apple")
    pass # run unittests to validate



from data import DICTIONARY
from data import LETTER_SCORES as SCORES_DICT

def load_words():
    """Load DICTIONARY file contents into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        content = file.readlines()
        wordlist = [line.strip() for line in content]
        return wordlist

def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate

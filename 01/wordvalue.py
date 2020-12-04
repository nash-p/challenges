from data import DICTIONARY
from data import LETTER_SCORES

def load_words(filename=DICTIONARY):
    """Load DICTIONARY file contents into a list and return list"""
    with open(filename, 'r') as file:
        content = file.readlines()
        words = [line.strip() for line in content]

    return words


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    letters = list(word.upper())
    for i in letters:
        value += LETTER_SCORES[i]

    return value
    

def max_word_value(wordlist=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    Returns a tuple of the word and its value"""
    old_word_value = 0
    for word in wordlist:
        word_value = calc_word_value(word)
        if word_value >= old_word_value:
            highest_word = word
            old_word_value = word_value
    
    return (highest_word, word_value)


if __name__ == "__main__":
    calc_word_value("apple")
    pass # run unittests to validate



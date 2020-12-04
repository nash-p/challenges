import re
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

    #This is necessary for things like apostrophes and hyphens)
    regex = re.compile('[^a-zA-Z]')
    word = regex.sub('', word)
    letters = list(word.upper())

    for i in letters:
        value += LETTER_SCORES[i]

    return value
    

def max_word_value(wordlist=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    NOTE: It does not return multiple words of equal value"""
    old_word_value = 0
    for word in wordlist:
        word_value = calc_word_value(word)
        if word_value >= old_word_value:
            highest_word = word
            old_word_value = word_value
    
    return highest_word


if __name__ == "__main__":
    
    pass # run unittests to validate



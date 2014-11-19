# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random
import re
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def ghost():
    print 'Welcome to Ghost!'
    currentPlayer1 = True
    print 'Player 1 Goes First.'
    currentWord = ''
    isLegal = True
    message = ""

    while message == "":
        if currentPlayer1 == True:
            currentPlayer = 1
        else:
            currentPlayer = 2
            
        print 'Current String: ' + currentWord
        currentLetter = raw_input('Player ' + str(currentPlayer) + '\'s letter: ').upper()
        if currentLetter in string.ascii_letters:
            currentWord += currentLetter
            message = isLosingWord(currentWord)
            if message == "":
                currentPlayer1 = not currentPlayer1
        else:
            print ('"' + str(currentLetter) + '" is not a valid entry. Please enter another letter.')

    print('Player ' + str(currentPlayer) + ' loses. ' + currentWord + ' ' + message)


def isLosingWord(testWord):
     testWord = testWord.lower()
     
    #test if the test word is in the dictionary
     if (testWord in wordlist) and (len(testWord) > 4):
        return "is a valid word."
    #test if this leads to any valid words
    regex = re.compile(testWord + '.*')
    possibleWords = [m.group(0) for l in wordlist for m in [regex.search(l)] if m]
    if len(possibleWords) == 0:
       return "does not lead to any valid words."

    return ""

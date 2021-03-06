# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

#Implemented in ch 6 to store a dictionary of all words and their values. Is called once on load
POINTS_DICT = {}

#Chapter 6, stores the time it takes to run a fixed number of operations.
TIME_LIMIT = 0.0

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

    get_words_to_points(wordlist)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    wordScore = 0
    for i in word:
        wordScore += SCRABBLE_LETTER_VALUES[i]
    if len(word) == n:
        wordScore += 50
    return wordScore
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...

    for letter in word:
        hand[letter] = hand[letter] -1
        if hand[letter] == 0:
            hand.pop(letter)
    return hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    # TO DO ...
    '''
    #commented out for lesson 6 to change this to a dictionary lookup
    if word_list.count(word) == 0:
        return False
    
    for i in word:
        if tempHand.get(i, 0) < word.count('i'):
            return False
    return True
    '''
    if word in POINTS_DICT:
        return True
    else:
        return False
#
# Problem #4: Playing a hand
#
def play_hand(hand):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    score = 0
    lastScore = 0
    time_limit = raw_input('Enter time, in seconds for players: ')
    total_time_used = 0
    try:
        time_limit = int(time_limit)
    except:
        time_limit = raw_input(str(time_limit) + ' is not a valid entry. Please enter a new time limit: ')
    
    display_hand(hand)

    start_time = time.time()
    #word = raw_input('Please enter your word: ') #removed for computer player
    word = pick_best_word(hand)
    end_time = time.time()
    time_used = end_time - start_time
    total_time_used += time_used

    TIME_LIMIT = get_time_limit(1)
    while len(hand) > 0 and word != '.':
        if time_limit > total_time_used:
            print 'It took you %.02f to provide an answer' % time_used
            print 'You have %.02f seconds left' % (time_limit - total_time_used)
            if is_valid_word(word, hand):
                lastScore = get_word_score(word, HAND_SIZE) 
                score += lastScore
                print ('Score for "' + word + '": ' + str(lastScore) + ' points')
                print ('Total Score: ' + str(score) + ' points')
                update_hand(hand, word)
                display_hand(hand)
                if len(hand) > 0:
                    start_time = time.time()
                    #word = raw_input('Please enter another word, or press "." to quit: ')
                    word = pick_best_word(hand)
                    end_time = time.time()
                    time_used = end_time - start_time
                    total_time_used += time_used
            else:
                start_time = time.time()
                word= raw_input('That word is not valid. Please enter another word: ')
                end_time = time.time()
                time_used = end_time - start_time
                total_time_used += time_used
    
        else:
            print 'Time limit exceeded'
            word = '.' #use this to escape out of the loop
            
            
    print ('Final Score: ' + str(score) + ' points')
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game():
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
       
    ## uncomment the following block of code once you've completed Problem #4

    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy())
            print
        elif cmd == 'r':
            play_hand(hand.copy())
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."
def pick_best_word(hand):
    #Return the highest scoring word from points_dict that can be made with the given hand.
    #Return '.' if no words can be made with the given hand
    lastList = []
    nextList = []
    handList = [] #these are the letters we're going to append 
    wordDict = {}
    currentWord = ""
    #makes initial list of the hand
    lastList.extend(hand)
    
    for i in range(1, len(hand)): # start at two since one adjusts the 
        for word in lastList: #make the list of letters to iterate over
            handList = []
            handList.extend(hand) #resets the handlist for each letter.    
            for letter in word: #when this is done it leaves us with just the remaining letters
                handList.remove(letter)
            for iterLetter in handList: #
                currentWord = word + iterLetter
                wordDict[currentWord] = POINTS_DICT.get(currentWord, 0) #creates the list of the first letter and all subsequent letters
                nextList.append(currentWord) #keep track of already tested combos to append the letters to next time
        lastList = copy.copy(nextList)
        nextList = []
    if wordDict == {}:
        return "."
    else:
        if max(wordDict.values()) == 0:
            return "."
        else:
            return max(wordDict, key = wordDict.get)
    

def get_words_to_points(word_list):
    #Return a dict that maps every word in word_list to its point value
    for word in word_list:
        POINTS_DICT[word] = get_word_score(word, HAND_SIZE)

def get_time_limit(k):
    """
 Return the time limit for the computer player as a function of the
multiplier k.
 points_dict should be the same dictionary that is created by
get_words_to_points.
"""
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in POINTS_DICT:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
        end_time = time.time()
    return (end_time - start_time) * k

def pickbest_word_faster:
    
    
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game()


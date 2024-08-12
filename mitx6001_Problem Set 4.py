# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#
# Student Name: Jasmin A. Feininger

import random
import string

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

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
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
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    return (len(word) * sum(SCRABBLE_LETTER_VALUES[i] for i in word)) +(50 if len(word) == n else 0)



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
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
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy() # makes copy of "hand"-dict which may be mutated to update used letters
    for i in word:
        updated_hand[i] = updated_hand[i] - 1
    return updated_hand



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    else:
        for i in word:                
            if word.count(i) > hand.get(i, 0):
                return False
        return True


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of total score:
    totalScore = 0
    output = "Run out of letters."

    # As long as there are still letters left in the hand:
    # Display hand, ask user for input, if input is a single period, end the game/break loop
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == '.':
            output = "Goodbye!"
            break

    # If input is not a single period:
        # If word is not valid, reject invalid word and print a message
        # If word is valid, output user how many points the word earned and the updated total score in one line
        # Update the hand
    # User entered '.' or ran out of letters, tell user total score

        else:
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.")
            else:
                score = getWordScore(word, n)
                totalScore += score
                print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore))
                hand = updateHand(hand, word)
    print('{0:s} Total score: {1:d} points.'.format(output, totalScore))
   
#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    hand = False
    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end the game').lower()
        if user_input not in 'nre':
            print('Invalid command.')
        else:
            if user_input == 'r' and not hand:
                print('You have not played a hand yet. Please play a new hand first!')
            elif user_input == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand.copy(), wordList, HAND_SIZE)
            elif user_input == 'r':
                playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                break
            print("")
   

# PART 2 FOLLOWS HERE:

from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    def calculateHandlen(hand):
        counts = hand.values()
        total = 0
        for i in range (len(counts)):
            total = total + counts[i]
        return total
        
    # Create a new variable to store the best word seen so far (initially None)
    # Create a new variable to store the maximum score seen so far (initially 0)

    bestword = None
    maxscore = 0

    # For each word in wordList: 
        # If word can be constructed from hand, determine how much word is worth:
            # If score for that word is higher than previous best score, update
            # best score and best word accordingly
    # Then return the best word you found
    
    for word in wordList:
        if isValidWord(word, hand, wordList) == True:
            score = getWordScore(word, calculateHandlen(hand))
            if getWordScore(word, calculateHandlen(hand)) > maxscore:
                maxscore = score
                bestword = word
    return bestword
   
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    while calculateHandlen(hand) > 0:
        print '\nCurrent Hand:',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if word is None:
            break
        hand = updateHand(hand, word)
        score_word = getWordScore(word, n)
        score += score_word
        print '"%s" earned %s points. Total: %s points' % (word, score_word, score)
    print 'Total score: %s points.' % (score)
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    hand = {}

    while True:
        user_input = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        
        if user_input == 'n':
            hand = dealHand(n)
            while user_input not in 'uc':    
                user_input = raw_input('Enter u to have yourself play, c to have the computer play:')
                if user_input not in 'uc':
                    print 'Invalid command.'
            if user_input == 'u':
                playHand(hand, wordList, n)
            elif user_input == 'c':
                compPlayHand(hand, wordList, n)
        
        elif user_input == 'r':
            if not hand:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                while user_input not in 'uc':    
                    user_input = raw_input('Enter u to have yourself play, c to have the computer play:')
                    if user_input not in 'uc':
                        print 'Invalid command.'
                if user_input == 'u':
                    playHand(hand, wordList, n)
                elif user_input == 'c':
                    compPlayHand(hand, wordList, n)
        
        elif user_input == 'e':
            break
        
        else:
            print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



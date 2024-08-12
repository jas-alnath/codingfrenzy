##Problem 1:
##Calculate the total amount of radiation a person was exposed to, using approximation.
##Function f calculates the radioactive decay curve for this problem.
##Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.

def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    result = 0
    while start < stop:
        result += f(start) * step
        start += step
    return result


##Problem 2 - Hangman Wordgame:
##Part 1, is the word guessed?
##We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed
##that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean -
##True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
##
##Example Usage:
##
##>>> secretWord = 'apple' 
##>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
##>>> print isWordGuessed(secretWord, lettersGuessed)
##False

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    temp_list = ""
    for c in secretWord:
        if c in lettersGuessed:
            temp_list += c
            if temp_list == secretWord:
                return True
        else:
            return False

##Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed.
##This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!
##
##Example Usage:
##
##>>> secretWord = 'apple' 
##>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
##>>> print getGuessedWord(secretWord, lettersGuessed)
##'_ pp_ e'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    temp_list = ""
    for c in secretWord:
        if c in lettersGuessed:
            temp_list += c
        elif c not in lettersGuessed:
            temp_list += '_ '
    return temp_list

##Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that
##is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
##
##Example Usage:
##
##>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
##>>> print getAvailableLetters(lettersGuessed)
##abcdfghjlmnoqtuvwxyz
##Note that this function should return the letters in alphabetical order, as in the example above.

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    letters_avail_list = []
    for l in alphabet:
        if l not in lettersGuessed:
            letters_avail_list.append(l)
            letters_avail = "".join(letters_avail_list)
    return letters_avail

##Hangman Part 2 - The game
##Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of
##Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and
##getAvailableLetters, that you've defined in the previous part.

def hangman(secretWord):
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is' , len(secretWord) , 'letters long.'
    print '-------------'
    total_guesses = 8
    while total_guesses > 0:
        print 'You have' , total_guesses , 'guesses left.'
        print 'Available Letters:' , getAvailableLetters(lettersGuessed)
        Guess= raw_input('Please guess a letter: ')
        Guess_letter = Guess.lower()
        if Guess_letter in secretWord and Guess_letter not in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Good guess:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        elif Guess_letter in secretWord and Guess_letter in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! You\'ve already guessed that letter:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
                break
        elif Guess_letter not in secretWord and Guess_letter not in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! That letter is not in my word:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            total_guesses -= 1
            if isWordGuessed(secretWord, lettersGuessed) == False and total_guesses == 0:
                print 'Sorry, you ran out of guesses. The word was else.'
        elif Guess_letter not in secretWord and Guess_letter in lettersGuessed:
            lettersGuessed += Guess_letter
            print 'Oops! You\'ve already guessed that letter:' , getGuessedWord(secretWord, lettersGuessed)
            print '-------------'
            if isWordGuessed(secretWord, lettersGuessed) == False and total_guesses == 0:
                print 'Sorry, you ran out of guesses. The word was else.'


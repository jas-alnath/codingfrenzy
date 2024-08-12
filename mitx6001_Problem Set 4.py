##Scrabble - A word game
##The first step is to implement some code that allows us to calculate the score for a single word.
##The function getWordScore should accept as input a string of lowercase letters (a word) and return
##the integer score for that word, using the game's scoring rules.

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

##A hand is the set of letters held by a player during the game. The player is initially dealt a set of random letters.
##For example, the player could start out with the following hand: a, q, l, m, u, i, l. In our program, a hand will be
##represented as a dictionary: the keys are (lowercase) letters and the values are the number of times the particular
##letter is repeated in that hand. For example, the above hand would be represented as:
##
##hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

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

##However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game.
##A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.

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

##We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function
##allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function,
##which can be done in under five lines of code.

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())


##Playing a hand:

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
    totalScore = 0
    output = "Run out of letters."
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == '.':
            output = "Goodbye!"
            break
        else:
            if not isValidWord(word, hand, wordList):
                print("Invalid word, please try again.")
            else:
                score = getWordScore(word, n)
                totalScore += score
                print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore))
                hand = updateHand(hand, word)
    print('{0:s} Total score: {1:d} points.'.format(output, totalScore))


##Playing a game:

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

##Now that you have completed your word game code, you decide that you would like to enable your computer (SkyNet)
##to play the game.
##In Part B you will make a modification to the playHand function from part A that will enable this to happen.

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    def calculateHandlen(hand):
        counts = hand.values()
        total = 0
        for i in range (len(counts)):
            total = total + counts[i]
        return total
     
    bestword = None
    maxscore = 0
    for word in wordList:
        if isValidWord(word, hand, wordList) == True:
            score = getWordScore(word, calculateHandlen(hand))
            if getWordScore(word, calculateHandlen(hand)) > maxscore:
                maxscore = score
                bestword = word
    return bestword

##Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand -
##in a manner very similar to Part A's playHand function (get the hint?).
##
##Implement the compPlayHand function. This function should allow the computer to play a given hand, using the procedure you just wrote
##in the previous part. This should be very similar to the earlier version in which a user selected the word, although deciding when it
##is done playing a particular hand will be different.

def compChooseWord(hand,wordList, n):
    bestword = None
    maxscore = 0
    for word in wordList:
        if isValidWord(word, hand, wordList) == True:
            score = getWordScore(word, calculateHandlen(hand))
            if getWordScore(word, calculateHandlen(hand)) > maxscore:
                maxscore = score
                bestword = word
    return bestword

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
        
##Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function.
##You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine
##the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.

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
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
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


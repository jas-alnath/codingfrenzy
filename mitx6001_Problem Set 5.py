##The Caesar Cipher
##Problem 1: Build the Shift Dictionary and Apply Shift

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        # creating empty dict to map shifted letters in
        cipher_dict = {}
        string_lo = string.ascii_lowercase
        string_up = string.ascii_uppercase
        
        # two loops for both lowercase & uppercase letters, if letter index plus shift is < 26
        # just map the shifted index in dict
        for letter in string_lo:
            if string_lo.index(letter) + shift < 26:
                cipher_dict[letter] = string_lo[string_lo.index(letter) + shift]
            else:
                cipher_dict[letter] = string_lo[string_lo.index(letter) - 26 + shift]

        for letter in string_up:
            if string_up.index(letter) + shift < 26:
                cipher_dict[letter] = string_up[string_up.index(letter) + shift]
            else:
                cipher_dict[letter] = string_up[string_up.index(letter) - 26 + shift]

        return cipher_dict                                        
            

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = self.build_shift_dict(shift)
        cipher_message = ""

        for char in self.message_text:
            if char in cipher:
                cipher_message = cipher_message + cipher[char]
            else: cipher_message = cipher_message + char
        return cipher_message


##Problem 2: Plaintext Message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

##Problem 3: Ciphertext Message

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        #self.message_text = get_message_text_encrypted()
        #self.valid_words = load_words(word_list)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # the emtpy tuple:
        best_shift = ()
        # counter for how many valid words found per shift:
        validWords_count = 0

        # decrypt_string stores message after first shift attempt
        # strings_list stores splitted decrypt_string in order to count the no. of valid words in it
        for s in range(26):
            decrypt_string = self.apply_shift(s)
            strings_list = decrypt_string.split(' ')
            wordcount = 0

            # if a valid word is found, increase counter for each one:
            for item in strings_list:
                if is_word(self.valid_words, item):
                    wordcount += 1

            if wordcount > validWords_count:
                validWords_count = wordcount
                best_shift = (s, decrypt_string)

        return best_shift

##Problem 4: Decrypt a Story

def decrypt_story():
    cipher_message = CiphertextMessage(get_story_string())
    return cipher_message.decrypt_message()
print decrypt_story()

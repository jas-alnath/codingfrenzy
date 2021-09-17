##Problem 3
##Write a function called dict_invert that takes in a dictionary with immutable values and
##returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary
##whose keys are the unique dictionary values in d. The value for a key in the inverse
##dictionary is a sorted list of all keys in d that have the same value in d.
##
##Here are some examples:
##
##If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
##If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
##If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

def dict_invert(d):
    inv_d = {}
    for k, v in d.items():
        keys = inv_d.setdefault(v, [])
        keys.append(k)
        keys.sort()
    return inv_d


##Problem 4 - Part 1
##Write a function called getSublists, which takes as parameters a list of integers named L
##and an integer named n.
##
##assume L is not empty
##assume 0 < n <= len(L)
##This function returns a list of all possible sublists in L of length n without skipping
##elements in L. The sublists in the returned list should be ordered in the way they appear
##in L, with those sublists starting from a smaller index being at the front of the list.
##
##Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should
##return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7],
##[4, 5, 7, 7], [5, 7, 7, 2]]
##
##Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the
##list [[1, 1], [1, 1], [1, 1], [1, 4]]

def getSublists(L, n):
    sublist = []
    for i in range(len(L) - n + 1):
        sublist.append(L[i:n+i])
    return sublist

##Problem 4 - Part 2
##Write a function called longestRun, which takes as a parameter a list of integers named L
##(assume L is not empty). This function returns the length of the longest run of monotonically
##increasing numbers occurring in L. A run of monotonically increasing numbers means that a
##number at position k+1 in the sequence is either greater than or equal to the number at
##position k in the sequence.
##
##For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the
##value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].

def getSublists(L, n):
    """
    L = list, n = int, assumes L is not empty, assumes 0 < n <= len(L)
    returns a list of all possible sublists in L of length n without skipping elements in L.
    The sublists in the returned list should be ordered in the way they appear in L,
    with those sublists starting from a smaller index being at the front of the list.
    n = number of subsets
    """
    return [L[i:i+n] for i in range(len(L)-n+1)]

def longestRun(L):
    """ takes: list of ints L, assumes L is not empty, returns the longest run of monotonically
    increasing numbers.
    """
    finalList = []
    run = 0
    for i in range(len(L)+1):
        for k in getSublists(L, i):
            finalList.append(k)
    for x in finalList:
        if sorted(x) == x and len(x) >= run:
            run = len(x)
    return run

##Problem 5
##In this problem, you will implement a class according to the specifications in the
##template file usresident.py.

class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        
        if status in ['citizen', 'legal_resident', 'illegal_resident']:
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status


##Problem 6
##Consider the following hierarchy of classes:
##class Person(object):     
##    def __init__(self, name):         
##        self.name = name     
##    def say(self, stuff):         
##        return self.name + ' says: ' + stuff     
##    def __str__(self):         
##        return self.name  
##
##class Lecturer(Person):     
##    def lecture(self, stuff):         
##        return 'I believe that ' + Person.say(self, stuff)  
##
##class Professor(Lecturer): 
##    def say(self, stuff): 
##        return self.name + ' says: ' + self.lecture(stuff)
##
##class ArrogantProfessor(Professor): 
##    def say(self, stuff): 
##        return 'It is obvious that ' + self.say(stuff)
##
##As written, this code leads to an infinite loop when using the Arrogant Professor class.
##Change the definition of ArrogantProfessor so that the following behavior is achieved:
##e = Person('eric') 
##le = Lecturer('eric') 
##pe = Professor('eric') 
##ae = ArrogantProfessor('eric')
##
##>>> e.say('the sky is blue')
##eric says: the sky is blue
##
##>>> le.say('the sky is blue')
##eric says: the sky is blue
##
##>>> le.lecture('the sky is blue')
##I believe that eric says: the sky is blue
##
##>>> pe.say('the sky is blue')
##eric says: I believe that eric says: the sky is blue
##
##>>> pe.lecture('the sky is blue')
##I believe that eric says: the sky is blue
##
##>>> ae.say('the sky is blue')
##eric says: It is obvious that eric says: the sky is blue
##
##>>> ae.lecture('the sky is blue')
##It is obvious that eric says: the sky is blue

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

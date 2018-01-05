import random
import time


def multi_thread():

    # create and start threads here
    # find the combination of words that all form a word and keep those in a
    # list
    

def thread_target():
    # find the combination of digits that combine to form words
    # these words will add up to give the word (Earth)
    words = []
    word = ""
    valid_words = ['EARTH','EAST', 'NORTH', 'SOUTH','WEST']

    # form a word
    for i in range()

def build_dict():
    # build random words from the letters given in a list
    # the letters are associalted with them, a digit,
    
    letters = ['A','E','H','N','O','R','S','T','U', 'W']

    # build a dictionary assigning random digits to letters
    # ensure that letters[keys] have different digits[keys]
    earth_dict = {}

    # get a sample of random digits
    digits = random.sample(xrange(0,10), 10)

    # associate letter to digit in a dictionary
    earth_dict = dict(zip(letters, digits))

    return  earth_dict

def build_words(earth_dict):
    
    # build a list of words
    words = []
    word = ""

    # list of valid words
    valid_words = ['EARTH','EAST', 'NORTH', 'SOUTH','WEST']

    # list of earth_dict keys
    letters = earth_dict.keys()

    # iterate to find a word 
    # then add the word to words
    # but you must ensure that all the words are different
    while(len(words) < 5):

        for i in range(5):
            # randomise the indices of letters going to word
            # add letter to word
            word += letters[random.randint(0,9)]


def validate_word(word, valid_words):
        # check if a word is valid
        if word in valid_words:
            words.append(word)
            valid_words.remove(word)
        elif word[:4] in valid_words:
            words.append(word[:4])
            valid_words.remove(word[:4])
        else:
            word = ""
       
# start the timer
ticks = time.time()
build_words(build_dict())
tocks = time.time()
print (tocks - ticks)

import random
import time
import numpy as np
import string

def validate_word(word):
    # find out if the given word is valid

    valid_words = ['EARTH','EAST', 'NORTH', 'SOUTH','WEST']

    return word in words

def markov():
    # build a markov model for the letters
    # find the occurence of each letter in the words and build probabilities
    letters = ['A','E','H','N','O','R','S','T','U', 'W']
    numbers = range(0,10)
    valid_words = ['EARTH','EAST', 'NORTH', 'SOUTH','WEST']

    # total number of letters in the set
    total_letters = 0
    letter_freq = {}

    for letter in letters:
        for word in valid_words:
            if letter in word:
                if letter in letter_freq:
                    letter_freq[letter] += 1
                else:
                    letter_freq[letter] = 1
                total_letters +=1
    print letter_freq, total_letters

def markov_2(text, test):
    # build a 26x26 matrix
    m = np.zeros((26,26))

    # grab a list of the letters
    alpha = list(string.ascii_lowercase)

    # turn transitions into probabilities
    counter_row = [ 0 for i in range(0,26)]

    # build the matrix M
    # iterate through the text
    for i in range(0, len(text)-1):
        # find the adjacent letters in the text
        x = text[i]
        y = text[i+1]

        # find the adjacent letters in the alphabet
        if x in alpha and y in alpha:
            x_i = alpha.index(x)
            y_i = alpha.index(y)
            
            # now update the transitions in the matrix m
            m[x_i][y_i] +=1
        
    # count all the transitions and turn them into probabilities
    for i in range(0,26):
        for j in range(0,26):
            counter_row[i] += m[i][j] 

    # now define matrix p, 26x26 and divide each of m[i][j] by counter[i] for
    # all pairs of i,j, thus, p[i][j] gives the probability of making that
    # transition from letter i to letter j
    p = np.zeros((26,26))

    for i in range(0,26):
        for j in range(0,26):
            if counter_row[i] != 0:
                p[i][j] = (m[i][j] / float(counter_row[i]))

    # time to test the model
         
    # initialise score 
    score  = 0

    # number of times we try to predict the letter
    attempts = 0


    for i in range(0, len(test) - 1):
        x = test[i]
        y = test[i+1]

        if x in alpha and y in alpha:
            x_i = alpha.index(x)
            y_i = alpha.index(y)

            # increment score and attempts
            score += p[x_i][y_i]

            attempts += 1

    # correct attempts,score/attempts
    accuracy =  score/float(attempts)

    return score, attempts, accuracy

def file_read(filename):
    # read a file and return text
    text = ""
    with open(filename, 'r') as f:
        text += f.readline()

    return text.lower()

# text the model
text = file_read('temp.txt')
test = file_read('test.txt')

print markov_2(text, test)

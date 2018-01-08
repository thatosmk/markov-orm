from sql_python import SQLPy
import pandas as pd
import numpy as np
from numpy.linalg import inv

class PyMarkov():

    def __init__(self, table_data):
        """ 
            build a markov model with absorbing states (r) and non-absorbing states
            (t)
        """
        absorbing = 0
        transient = 0
        for row in table_data:
            transient += 1
            absorbing = len(row)

        self.r = absorbing - transient
        self.t = transient
        self.data = table_data
    
    def abs_states(self):
        """ return the number of absorbing states """
        return self.r

    def trans_states(self):
        """ return the number of transient states """
        return self.t

    def get_transient_matrix(self, matrix):
        """ return non-absorbing matrix"""
        t = self.t
        r = self.r
        return matrix[:t,r+2:]

    def get_abs_matrix(self, matrix):
        """ return absorbing matrix"""
        t = self.trans_states()
        r = self.abs_states()
        return matrix[:t,:t]


    def get_matrix_array(self):
        """ given a database table, return the transition matrix """
        matrix_arr = []

        # create an array from the rows of the database table
        for row in self.data:
            matrix_arr.append(list(row))

        return np.array(matrix_arr)


    def get_row_sum(self):
        """ make row calculations on the array matrix with data from the table
        """
        return np.sum(self.get_matrix_array(), axis=1)


    def get_col_sum(self):
        """ make col calculations on the array matrix with data from the table
        """
        return np.sum(self.get_matrix_array(), axis=0)


    def get_trans_matrix(self):
        """ given a database table, return the transition matrix """
        matrix_arr = []

        # create an array from the rows of the database table
        for row in self.data:
            matrix_arr.append(list(row))
       
        # row sum calculations
        row_sum = np.sum(matrix_arr, axis=1)
        # column sum calculations
        col_sum = np.sum(matrix_arr, axis=0)

        # convert to an n*n array 
        markov_matrix = np.array(matrix_arr)

        # find the transitional matrix, give it same size as markov-matrix
        transition= markov_matrix

        # divide each row in the array by the total sum of that row
        for i in range(0, len(row_sum)):
            for j in range(0, len(col_sum)):
                # divide each item by sum of its row
                transition[i][j] =              round(float(markov_matrix[i][j])/float(row_sum[i]), 4)

        return np.array(transition)


    def time_to_absorb(self, c_state):
        """ from current state c_state, how many iterations are needed to reach
        absorption """
        # t = Nc
        c = np.transpose(c_state)
        # a dot product does matrix multiplication for np.arrays
        return n_matrix.dot(np.transpose(c))


    def compute(self, matrix):
        """
         define the canonical form of the arbitrary arbsorbing markov chain
         renumber the states so that the transient states come first
         if there are --r-- absorbing states, and --t-- transition states, the
         canonical form will involve a --r-by-r-- identity matrix
        """ 
        # convert matrix into a canonical form for a markov transition matrix
        # indentity matrix is r-by-r
        # slice the matrix to get a smaller matrix according to the canonical form
        # groupings, slicing works like -- matrix[row[:], col[:]]
        # r-by-r matrix
        id_matrix = matrix[self.r+1:,self.r+1:]
        # r-by-t matrix
        zero_matrix = matrix[self.r+1:,:self.t]
        # t-by-r matrix
        r_matrix = matrix[:self.t,self.r+2:]

        # therefore your non-absorbing matrix is t-by-t
        q_matrix = matrix[:self.t,:self.t]

        # you also need a t-by-t identity matrix
        i_q = np.identity(self.t)

        # compute the matrix N(fundamental matrix for the absorbing markov chain),
        # the entry n_{ij} the number of times that a process
        # is in the transient state s_j if it started in transient state s_i
        n_matrix = inv(i_q - q_matrix )


        """ now find the absorption probabilities
            this is a t-by-r matrix and its entries  give the probability that an
            absorbing chain will be absorbed in the absorbing state s_j if it starts
            in the transient state s_i
            B = NR
        """
        # use this to calculate the repaid and write off amounts
        b_matrix = n_matrix.dot(r_matrix)
        
        eventual_matrix = np.transpose(b_matrix).dot(self.get_row_sum())

        return eventual_matrix

    # currently not working as expected
    def forecast(self, n):
        """ given the number of months, show a markov forecast """
            pass


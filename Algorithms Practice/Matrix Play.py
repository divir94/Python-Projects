# -*- coding: utf-8 -*-
##Problem:
##Given a matrix, you need to create another matrix such that the value (i,j) is either -1, 0 or 1. 
##1 - if multiplication of all values in ith row and jth column is greater than 0. 
##-1 - if multiplication of all values in ith row and jth column is less than 0. 
##0 - if multiplication of all the values in ith row and jth column is 0. 
##
##Example:
##1 2 3 1
##1 0 -1 2
##-1 1 1 1
##
##-1 0 -1 1
##0 0 0 0
##1 0 1 -1

def flip(matrix, i, j):
    if (matrix[i][j] == 0): return 0
    elif (matrix[i][j] == 1): return -1
    elif (matrix[i][j] == -1): return 1
    else:
            print 'undefined value'
            return Null


def encode(matrix):
    # Num of rows and columns
        rows = len(matrix)
        cols = len(matrix[0])
        # Initialize new_matrix to all 1’s
        new_matrix = [ [1 for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                # If 0, set ith row and jth column to 0
                if(matrix[i][j] == 0):
                    # Set jth column to 0
                    for x in range(rows):
                        new_matrix[x][j] = 0
                    # Set ith column to 0
                    for y in range(cols):
                        new_matrix[i][y] = 0
                # If pos, skip
                elif(matrix[i][j] > 0):
                    pass
                # If neg, flip sign for ith row and jth column
                elif(matrix[i][j] < 0):
                    for x in range(rows):
                        new_matrix[x][j] = flip(new_matrix, x, j)
                    for y in range(cols):
                        new_matrix[i][y] = flip(new_matrix, i, y)
                else: 
                    print ('new matrix value is other than 0,1,-1')
                    return matrix
        return new_matrix

matrix = [[1,2,3,1], [1,0,-1,2], [-1,1,1,1]]

def print_row(row): print row
print 'Input'
[print_row(row) for row in matrix]
print '\nOutput'
[print_row(row) for row in encode(matrix)]


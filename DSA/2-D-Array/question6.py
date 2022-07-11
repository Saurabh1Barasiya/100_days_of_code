# take column wise input from user .
# and use numpy to create a matrix.

import numpy as np

rows = int(input("Please enter the rows : "))
column = int(input("Please enter the column : "))

matrix = np.zeros((rows, column),dtype=int) 

for i in range(column):
    for j in range(rows):
        print((j,i))
        matrix[j][i] = int(input())

for i in range(rows):
    for j in range(column):
        print(matrix[i][j], end = " ")
    print("")


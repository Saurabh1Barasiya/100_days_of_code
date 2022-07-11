# with thew help of numpy we take input and show output.

import numpy as np
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns:"))
matrix = np.zeros((rows,columns),dtype=int)
# print(matrix)

# input from row wise input.
for i in range(rows):
    for j in range(columns):
        print((i,j),end = " ")
        matrix[i][j] = int(input())

# oputput the matrix.   
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print()
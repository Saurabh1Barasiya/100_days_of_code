# input using numpy.

import numpy as np
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns:"))
matrix = np.zeros((rows,columns),dtype=int)
print(matrix)

# take input .
for i in range(columns):
    for j in range(rows):
        # matrix[i][j] = int(input())
        print((j,i),end = " ")
        input()
    print()

# print the matrix.
# for i in range(columns):
#     for j in range(rows):
#         a = (i,j)
#         print( a ,end = "  ")
#     print()

# search element present is not.

import numpy as np
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initialize a matrix.
matrix = np.zeros((rows, columns),dtype=int)
# print(matrix)

# for input.
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = int(input())

target = int(input("Enter the target number: "))

#  👇👇👇👇👇👇👇👇👇👇👀👀

check = False
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == target:
            print("Target found at index ",(i,j))
            check = True
            break
    else:
        if check:
            break
        print("Not found")
    



# for output.
# for i in range(rows):
#     for j in range(columns):
#         print(matrix[i][j], end = " ")
#     print()
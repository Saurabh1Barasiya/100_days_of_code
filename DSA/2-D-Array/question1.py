# How to input 2-d Array in python.
# A basic code for matrix input from user

# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")

# For user input
# for i in range(R):		 # A for loop for row entries
# 	a =[]
# 	for j in range(C):	 # A for loop for column entries
# 		a.append(int(input()))
# 	matrix.append(a)

 
# # For printing the matrix
# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " 

# 👀👀👀👀👀👀👀👀👀👀👀👇👇

# Enter 2-d Array in python.

matrix = []
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
# print("Array element inserted ", matrix)

# for row in matrix:
#     print("Row ", row)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print()


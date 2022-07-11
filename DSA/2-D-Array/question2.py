# take input from list comprehension.

print("Please enter the row size.")
row = int(input())
print("Please enter the column size.")
col = int(input())

matrix = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix is:",matrix)

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print()

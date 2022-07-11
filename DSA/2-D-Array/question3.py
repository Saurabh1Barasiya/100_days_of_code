#  Take input and show output.

print("Enter column size: " )
col = int(input())
print("Enter row size: ")
row = int(input())

matrix = []
print("Enter the matrix: ")

for i in range(col):
    a = []
    for j in range(row):
        a.append(int(input()))
    matrix.append(a)    # append the list to the matrix

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print()
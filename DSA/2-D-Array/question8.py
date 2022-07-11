# Get row wise sum .


# 👀👀👀👀👀👇👇👇👇👇
# sort solution pythonic way.
# def get_rwo_sum(matrix,row,col):
#     for i in range(row):
#         print(sum(matrix[i]))


def get_row_sum(matrix,row,col):
    print("Row wise sum ")
    for i in range(row):
        ans = 0
        for j in range(col):
            ans += matrix[i][j]
        print(ans)


def get_col_sum(matrix,row,col):
    print("column wise sum ")
    for i in range(col):
        ans = 0
        for j in range(row):    
            ans += matrix[j][i]
        print(ans)


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    get_row_sum(matrix,3,3)
    get_col_sum(matrix,3,3)
    print(matrix)
    
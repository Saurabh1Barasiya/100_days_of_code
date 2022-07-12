# get sum of 2-d Array in python.
def get_sum(matrix,row,col):
    sum_ = 0
    for i in range(row):
        for j in range(col):
            sum_ += matrix[i][j]
    return sum_

if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    row = 3
    col = 3
    ans = get_sum(matrix, row, col)
    print(ans)
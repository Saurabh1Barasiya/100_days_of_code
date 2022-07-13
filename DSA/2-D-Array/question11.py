# get largest maximum row index.

def get_max_row_index(matrix,row,col):
    max_row = 0
    
    large_sum = 0
    for i in range(row):
        sum_ = 0
        for j in range(col):
            sum_ += matrix[i][j]
        if sum_ > large_sum:
            large_sum = sum_
            max_row = i
    return max_row

if __name__ == '__main__':
    matrix = [
        [1, 2 ,100],
        [4, 5, 60],
        [7, 8, 200],
    ] 
    row = 3
    col = 3
    ans = get_max_row_index(matrix,row,col)
    print(ans)

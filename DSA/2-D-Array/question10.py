# get digonal elements sum.
def get_diog_sum(matrix,row,col):
    d_sum = 0
    for i in range(row):
        for j in range(col):
            if i==j:
                #print("Match found ",(i,j))
                d_sum += matrix[i][j]
    return d_sum


def get_diog_sum_right(matrix,row,col):
    r_sum = 0
    col = col-1
    for i in range(row):
        j = col - i
        r_sum += matrix[i][j]
    return r_sum


if __name__ == '__main__':
    matrix = [
        [1, 2 ,3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    ans = get_diog_sum(matrix,3,3)
    print(ans)
    ans1 = get_diog_sum_right(matrix,3,3)
    print(ans1)

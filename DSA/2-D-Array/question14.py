# rotate 90 degree matrix . means print with 90 degree.
def print_90_degree_matrix(matrix,row,col):
    start_col = 0
    start_row = 0
    end_row = row-1
    count = 0
    totel = row * col
    degree_90 = []
    while count < totel:
        # print first column.
        for i in range(end_row,start_row-1,-1):
            if count < totel:
                print(matrix[i][start_col],end=" ")
                degree_90.append(matrix[i][start_col])
                count += 1
        start_col += 1    

if __name__ == '__main__':
    matrix = [
        [1, 2 ,3],
        [4, 5, 6],
        [7, 8, 9],
        [10,11,12]
    ]
    row = 4
    col = 3
    ans = print_90_degree_matrix(matrix,row,col)
    # for i in range(col):
    #     for j in range(row)

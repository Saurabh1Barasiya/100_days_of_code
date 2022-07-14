# print spiral matrix


def print_spiral_matrix(matrix,row,col):
    start_row = 0
    start_col = 0
    end_row = row-1
    end_col = col-1
    count = 0
    totel = row * col
    while count < totel:
        # print first row.
        for i in range(start_col,end_col+1):
            if count < totel:
                print(matrix[start_row][i],end=" ")
                count += 1
        start_row += 1

        # print last column.
        for i in range(start_row,end_row+1):
            if count < totel:
                print(matrix[i][end_col],end=" ")
                count += 1
        end_col -= 1

        # print last row.
        for i in range(end_col,start_col-1,-1):
            if count < totel:
                print(matrix[end_row][i],end=" ")
                count += 1
        end_row -= 1

        # print first column.
        for i in range(end_row,start_row-1,-1):
            if count < totel:
                print(matrix[i][start_col],end=" ")
                count += 1
        start_col += 1

if __name__ == '__main__':  
    matrix = [
        [1, 2 ,3],
        [4, 5, 6],
        [7, 8, 9]
        # [1, 2 ,3, 4],
        # [5, 6, 7, 8],
        # [9, 10, 11, 12],
    ]
    row = 3
    col = 3
    ans = print_spiral_matrix(matrix,row,col)
    # for i in ans:
    #     print(i,end=" ")

# print like a wave.
def print_spiral_matrix(matrix,row,col):
    final = []
    for c in range(col):
        if c % 2== 0:
            for r in range(row):
                # print(matrix[r][c],end=" ")
                final.append(matrix[r][c])
        else:
            for r in range(row-1,-1,-1):
                # print(matrix[r][c],end=" ")
                final.append(matrix[r][c])
    return final

if __name__ == '__main__':
        matrix = [
            [1, 2 ,3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        row = 3
        col = 3
        ans = print_spiral_matrix(matrix,row,col)
        for i in ans:
            print(i,end=" ")
# binary search in 2-d Array (matrix).

# search in sorted row as well as sotetd column.

'''
def binary_search_in_2_d_matrix(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    start = 0
    end = (row*col) - 1
    mid = start+(end-start)//2
    while start <= end:
        if matrix[mid//col][mid%col] == target:
            return 1
        if target > mid:
            start = mid+1
        if target < mid:
            end = mid-1
        mid = start+(end-start)//2
    return 0
'''

def serch_in_sorted_row_and_sorted_column(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    row_index = 0
    col_index = col-1
    while row_index < row and col_index >= 0:
        element = matrix[row_index][col_index]
        
        if target == element:
            # print(row_index,col_index)
            return 1

        if target > element :
            row_index += 1
        else:
            col_index -= 1

if __name__ == '__main__':
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ]
    target = 7
    # ans = binary_search_in_2_d_matrix(matrix, target)

    ans = serch_in_sorted_row_and_sorted_column(matrix, target)
    if ans:
        print("Element found")
    else:
        print("Element not found")


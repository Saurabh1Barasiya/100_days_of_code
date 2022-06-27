# find piviot element(index) in array.
# 
# # arr = [0,10,5,2]

def binary_search_pivit_element_index(array):
    start = 0
    end = len(array)-1
    mid = start+(end-start)//2
    while start < end:
        if array[mid] >= array[0]:
            start = mid + 1
        else:
            end = mid
        mid = start+(end-start)//2
    return start

arr = [3,8,10,17,1]
# arr = [7,9,1,2]
print(binary_search_pivit_element_index(arr))
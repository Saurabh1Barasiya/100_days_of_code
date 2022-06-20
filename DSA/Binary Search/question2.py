# [1,2,3,3,5]
# minimum index 2.
# maximum index 3.

# find left most index and right most index of the key in the array.
# using binar search.

def binary_search_left_most_occurrences(arr,size,key):
    start  = 0
    end = size - 1
    mid = start+(end-start)//2
    ans = -1
    while start <= end:
        if key == arr[mid]:
            ans = mid
            end = mid - 1
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        mid = start+(end-start)//2
    return ans

def binary_search_right_most_occurrences(arr,size,key):
    start  = 0
    end = size - 1
    mid = start+(end-start)//2
    ans = -1
    while start <= end:
        print("-----------------",arr[mid])
        if key == arr[mid]:
            ans = mid
            start = mid + 1
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        mid = start+(end-start)//2
    return ans

if __name__ == "__main__":
    arr = [1,2,3,3,5]
    size = len(arr)
    key = 3
    ret_val_1 = binary_search_left_most_occurrences(arr,size,key)
    ret_val_2 = binary_search_right_most_occurrences(arr,size,key)
    print("left most index:",ret_val_1)
    print("right most index:",ret_val_2)
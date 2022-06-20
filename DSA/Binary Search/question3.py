# [1,2,3,3,5]
# find left most index and right most index of the key in the array.
# using binar search.


# binary search always sorted elements par hi apply hogi.
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
        if key == arr[mid]:
            ans = mid
            start = mid + 1
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        mid = start+(end-start)//2
    return ans


# find left most index and right most index of the key in the array.
# using binar search.
if __name__ == "__main__":
    arr = [1,1,2,3,3,3,3,5]
    size = len(arr)
    key = 3
    first = binary_search_left_most_occurrences(arr,size,key)
    last = binary_search_right_most_occurrences(arr,size,key)
    print("left most index:",first)
    print("right most index:",last)
    print(f"totel number of occurrences of key {key} is {(last-first)+1}")
    

# Binary search using recursion.

# Binary search apply on sorted array.

def binary_Search_recursion(arr,start,end,key):
    # Base case
    if start > end:
        return False
    
    # get mid
    mid  = start+(end-start)//2
    if arr[mid] == key:
        return True
    
    if key > arr[mid]:
        # Recursive case. 
        # go to right side.
        return binary_Search_recursion(arr,mid+1,end,key)
    else:
        # Recursive case.
        # go to left side.
        return binary_Search_recursion(arr,start,mid-1,key)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
    start = 0
    end = len(array)-1
    key = 10
    ans = binary_Search_recursion(array, start, end,key)
    print(ans)
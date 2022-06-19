# Binary search program.
def binary_search(arr,size,key):
    start = 0 
    end = size - 1
    mid = start+(end-start)//2  # mid is the middle index of the array
    while start <= end: 
        if key == arr[mid]:
            print("value found",arr[mid])
            return mid
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = start+(end-start)//2
    return -1
        

arr = [25,45,30,78,22,10,11,12,13,14]
arr.sort()
print(arr) #[10, 11, 12, 13, 14, 22, 25, 30, 45, 78]
size = len(arr)
key = 22
ret_val = binary_search(arr,size,key)
if ret_val == -1:
    print("value not found")
else:
    print("value found at index",ret_val)
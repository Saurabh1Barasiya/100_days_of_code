# reverse an array.

def swap_end_begain(arr):
    mid = len(arr) // 2
    i = 0
    while i < mid:
        arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
        i += 1
    return arr
# arr = [6,5,4,3,2,1]
arr = [10,15,25,30,50]
swap_end_begain(arr)
print(arr)
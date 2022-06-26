# Peek index in a montned array.
def find_max_value_index(arr):
    start  = 0
    end = len(arr)-1
    mid = start+(end-start)//2
    while start < end:
        if arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid
        mid = start+(end-start)//2
    return start

# arr = [0,10,5,2]
# arr = [3,4,5,1]
arr = [24,69,70,100,90,80,60,50]
print(find_max_value_index(arr))

# in binary search sorted hona jaruri h cahe asending or desending.
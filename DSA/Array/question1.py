# find maximum and minimum value in a array;

def get_max(arr):
    i = 0
    max = 0
    while i < len(arr):
        if arr[i] > max:
            max = arr[i]
        i += 1
    return max

def get_min(arr):
    min = arr[0]
    i = 1
    while i < len(arr):
        if min > arr[i]:
            min = arr[i]
        i += 1
    return min
    
arr = [10,20,4,5,64,78,100]
print("Minimum element of this array",get_min(arr))
print("Maximum element of this array",get_max(arr))
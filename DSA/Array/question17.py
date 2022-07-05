# move zeros to the right positions --> Love babber solution.

def move_zeros_to_right(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
        j += 1
    return arr
arr = [0,0,1,2]
ans = move_zeros_to_right(arr)
print(ans)
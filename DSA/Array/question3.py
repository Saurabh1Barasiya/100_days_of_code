# swap alternative elements in an array.
def alter_swap(arr):
    i = 0
    while i < len(arr):
        if i+1 < len(arr):
            arr[i], arr[i+1] = arr[i+1], arr[i] 
        i+= 2
arr = [1,2,3,4,5,]
alter_swap(arr)
print(arr)

'''
def alter_swap(arr):
    i = 0
    if len(arr) %2 ==0:
        while i < len(arr):
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 2
    else:
         while i < len(arr)-1:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 2
    return arr
arr = [1,2,3,4,5,6]
alter_swap(arr)
print(arr)
'''
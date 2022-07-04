# Reverse after an index.

def change_array_at_index(arr,index):
    start = index+1
    end = len(arr)-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1

# arr = [10,9,8,6,7]
arr = [1,2,3,4,5,6]
index = 3
print("Before sortinng array " ,arr)
change_array_at_index(arr,index)
print("After sortinng array  ",arr)
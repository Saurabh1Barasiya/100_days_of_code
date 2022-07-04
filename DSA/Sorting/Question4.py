def Insertion_Sort(arr):
    i = 1
    while i < len(arr):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        i += 1
arr = [34,15,29,8,50,1,2,3]
print("Before sortinng array ",arr)
Insertion_Sort(arr)
print("After sortinng array  ",arr)
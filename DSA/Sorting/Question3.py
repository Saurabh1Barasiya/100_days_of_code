# Insertion sort Algorithm Time Complexity: O(n^2)
# Insertion sort Algorithm Space Complexity: O(1)
# Best case Time Complexity: O(n)
# Worst case Time Complexity: O(n^2)
# Average case Time Complexity: O(n^2)

def Insertion_Sort_Algorithm(arr):
    i = 1
    while i < len(arr):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        i += 1
arr = [5,6,4,3,2,1,11,1,]
print("Before sortinng array ",arr)
Insertion_Sort_Algorithm(arr)
print("After sortinng array  ",arr)


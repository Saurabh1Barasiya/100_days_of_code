# Selection sort Algorithm.

def Selection_sort(arr):
    i = 0
    while i < len(arr)-1:
        mini_index = i 
        j = i+1
        while j < len(arr):
            if arr[mini_index] > arr[j]:
                arr[mini_index],arr[j] = arr[j],arr[mini_index]
            j += 1
        # print("Minimum value",arr[mini_index])
        i+=1
# arr = [7,1,4,3,9]
# arr = [7,1,4,3,9,85,4,5,2]
arr = [7,1,4,3,9,5,2,0]
print("Before sortinng array ",arr)
Selection_sort(arr)
print("After sortinng array  ",arr)

# 👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀
# Worst case Time Complexity: O(n^2)
# Best case Time Complexity: O(n^2)
# Average case Time Complexity: O(n^2)
# Space Complexity: O(1)
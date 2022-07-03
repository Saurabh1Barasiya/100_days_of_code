# Bubble sort Algorithm.
# Time complexcity worst case O(n^2)
# Time complexcity best case O(n)
# Time complexcity average case O(n^2)
# Space complexity O(1)

def bubbleSortAlgorithm(arr):
    i = 0
    while i < len(arr)-1:
        print(f"Round {i} and array {arr}")
        j = 0
        while j < len(arr)-1-i:
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j += 1
        i += 1  # i = i+1

arr = [10,1,7,6,9]
print("Before sortinng array ",arr)
bubbleSortAlgorithm(arr)
print("After sortinng array  ",arr) 

print("-----------------------------------------------------------------")

# 👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀
def bubbleSortAlgorithm(arr):
    i = 0
    while i < len(arr)-1:
        print(f"Round {i} and array {arr}")
        j = 0
        swap = False
        while j < len(arr)-1-i:
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
            j += 1
        if swap == False:
            break
        i += 1  # i = i+1

arr = [10,1,7,6,9]
print("Before sortinng array ",arr)
bubbleSortAlgorithm(arr)
print("After sortinng array  ",arr) 

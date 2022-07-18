# bubble sort using recursion.

# def bubbleSortAlgorithm(arr):
#     i = 0
#     while i < len(arr):
#         j = 0
#         while j < len(arr)-1-i:
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#             j += 1
#         i += 1
#     return arr


def bubblesort_recursion(arr,size):
        # base case.
        if size == 0 :
            return

        # preprocessing
        i = 0
        while i < size:
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i += 1
        
        # recursive case.
        bubblesort_recursion(arr,size-1)
        return arr
        


if __name__ == '__main__':
    arr = [10,1,2,4,0]
    size = len(arr)-1
    ans = bubblesort_recursion(arr,size)
    print(ans)     
# selection sort using recursion.

'''
def selection_sort(arr):
    i = 0
    while i < len(arr)-1:
        j = i + 1
        min_index = i
        while j < len(arr):
            if arr[min_index] > arr[j]:
                arr[min_index],arr[j] = arr[j],arr[min_index]
                print(arr)
            j += 1
        i += 1
    return arr
arr = [8,4,1,5,9,2]
selection_sort(arr)
'''

def selection_sort_recursion(arr,start,size):
    # print("star==",start)
    if start == size-1:
        return
    i = start
    min_index = i   # min_index is the index of the minimum element.
    j = i + 1
    while j < size:
        if arr[min_index] > arr[j]:
            arr[min_index],arr[j] = arr[j],arr[min_index]
        j+=1
    # print(arr[start::])
    print(arr)
    selection_sort_recursion(arr,start+1,size)
    return arr
if __name__ == '__main__':
    arr = [8,4,1,5,9,2]
    start = 0
    size = len(arr)   # size = 5
    ans = selection_sort_recursion(arr,start,size)
    # print(ans)
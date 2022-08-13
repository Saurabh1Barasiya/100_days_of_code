# optimized merge sort algorithm .
# ham yaha par original array me changes kar dete h.

def merge_two_sorted_array(left,right, arr):
    first_length = len(left)
    secound_length = len(right)

    i = j = k = 0

    while i < first_length and j < secound_length:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1        
        k += 1
    
    while i < first_length:
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < secound_length:
        arr[k] = right[j]
        k += 1
        j += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge_two_sorted_array(left,right, arr)

arr = [5,6,2,1,0]
merge_sort(arr)
print(arr)






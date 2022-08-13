# merge sort algorithm.

# space bhut jyada. use ho raha h .

def merge_two_sorted_array(left,right):
    sorted_array = []

    first_length = len(left)
    secound_length = len(right)

    i = j = 0

    while i < first_length and j < secound_length:
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    while i < first_length:
        sorted_array.append(left[i])
        i += 1
    
    while j < secound_length:
        sorted_array.append(right[j])
        j += 1

    return sorted_array


def merg_sort(arr):

    # 2 // 2 = 1
    # 0 nahi hota.

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merg_sort(left)
    right = merg_sort(right)

    return merge_two_sorted_array(left,right)


arr = [5,6,2,1,0]
print(merg_sort(arr))

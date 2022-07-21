# optimize merge sort.

def merge_two_array_sorted_menner(first, secound, arr):
    i = j = k = 0
    len_first = len(first)
    len_secound = len(secound)

    while i < len_first and j < len_secound:
        if first[i] < secound[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = secound[j]
            j += 1
        k+=1

    while i < len_first:
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len_secound:
        arr[k] = secound[j]
        j += 1
        k += 1



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # print("before ",left, right)
    merge_sort(left)
    merge_sort(right)
    # print("after ",left, right)
    merge_two_array_sorted_menner(left, right, arr)

if __name__ == '__main__':
    arr = [7,5,2,0,4,6,8,9,3,1]
    merge_sort(arr)
    print(arr)



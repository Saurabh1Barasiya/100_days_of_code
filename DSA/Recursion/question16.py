def merge_two_array_sorted_menner(arr1, arr2):
    sorted_array = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1
    # remaining elements of array 1.
    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1

    # remaining elements of array 2.
    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array


def megre_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = megre_sort(left)
    right = megre_sort(right)
    return merge_two_array_sorted_menner(left, right)


if __name__ == '__main__':
    # arr = [9,8,7,2,1,0,2,14,5,23,6,7,8,5,9]
    arr = [5,8,3,6,9,7]
    ans = megre_sort(arr)
    print(ans)
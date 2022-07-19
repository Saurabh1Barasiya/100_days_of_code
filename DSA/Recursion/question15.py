# insertion sort algo.

# def insertion_sort(arr):
#     i = 1
#     while i < len(arr):
#         temp = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > temp:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = temp
#         i += 1
#     return arr

def insertion_sort_algo(arr,size,length):
    if size == length:
        return
    temp = arr[size]
    j = size-1
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp
    insertion_sort_algo(arr,size+1,length)
    return arr

if __name__ == '__main__':
    arr = [8,4,1,5,9,2,0,3,15]
    length = len(arr)
    size = 1
    ans = insertion_sort_algo(arr,size,length)
    print(ans)
    
# find piviot element(index) in array.
# and search element in the array.
# # arr = [0,10,5,2]

def binary_search(arr,s,e,key):
    start = s
    end = e
    mid = start+(end-start)//2  # mid is the middle index of the array
    while start <= end: 
        if key == arr[mid]:
            print("value found",arr[mid])
            return mid
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = start+(end-start)//2
    return -1



def binary_search_pivit_element_index(array):
    start = 0
    end = len(array)-1
    mid = start+(end-start)//2
    while start < end:
        if array[mid] >= array[0]:
            start = mid + 1
        else:
            end = mid
        mid = start+(end-start)//2
    return start


def find_position(arr,n,k):
    piviot  =  binary_search_pivit_element_index(arr)
    if k>= arr[piviot] and k<= arr[n-1]:
        # bs in first line
        return binary_search(arr,piviot,len(arr)-1,k)
    else:
        # bs in second line
        return binary_search(arr,0,piviot-1,k)

if __name__ == "__main__":
    arr = [3,8,10,17,1]
    print(find_position(arr,5,3))


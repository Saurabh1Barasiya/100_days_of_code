# merge two sorted array version 2:

def merge_sorted_array(arr,start,end):
    mid = (start+end)//2
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    # print(left,right)
    left.sort()
    right.sort()
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i < len(left):
        arr[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1


if __name__ == '__main__':
    arr = [10,20,40,50,30,45,78,96,41,23]
    start = 0
    end = len(arr)-1
    merge_sorted_array(arr,start,end)
    print(arr)
    
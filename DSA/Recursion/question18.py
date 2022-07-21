# Quick sort algorithm.

def partition(arr,start,end):
    piviot = arr[start]   
    count = 0 
    k = start+1
    while k <= end:
        if arr[k] < piviot:
            count += 1
        k += 1

    piviot_index = count + start
    arr[start],arr[piviot_index] = arr[piviot_index],arr[start]

    # handle left and right part.

    i = start
    j = end

    while i < piviot_index and j > piviot_index:
        while arr[i] < piviot:
            i+=1     
        
        while arr[j] > piviot:
            j-=1

        if i < piviot_index and j > piviot_index:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

    return piviot_index

        

def queck_sort(arr,start,end):
    if start >= end:
        return
    p = partition(arr,start,end)
    queck_sort(arr,start,p-1)
    queck_sort(arr,p+1,end)

if __name__ == "__main__":
    arr = [8,5,1,2,9,0]
    start = 0
    end = len(arr) - 1
    queck_sort(arr,start,end)
    print(arr)
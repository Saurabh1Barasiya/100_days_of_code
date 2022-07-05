# Merge two sorted array.
def merge(arr1,n,arr2,m):
    i = 0
    j = 0
    l3 = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            l3.append(arr1[i])
            i+=1
        else:
            l3.append(arr2[j])
            j+=1

    # copy first array.       
    while i < n:
        l3.append(arr1[i])
        i+=1

    # copy second array.
    while j < m:
        l3.append(arr2[j])
        j+=1
    return l3

if __name__ == "__main__":
    arr1 = [1,3,5,7,9]
    arr2 = [2,4,6] 
    n = len(arr1)
    m = len(arr2)
    ans = merge(arr1,n,arr2,m)
    print("Merged array ",ans)
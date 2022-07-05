def merge_sorted(arr1,arr2):
    c = 0
    i = 0
    while i < len(arr1):
        if arr1[i] == 0:
            arr1[i] = arr2[c]
            c+=1
        i+=1
    arr1.sort()
    return arr1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge_sorted(nums1,nums2))
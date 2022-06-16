# Intersection of two array.
'''
def get_intersection(arr1, arr2):
    l2 = []
    for value1 in arr1:
        for index,value2 in enumerate(arr2):
            if value1 == value2:
                l2.append(value1)
                del arr2[index]
    return l2
arr1 = [1,2,2,2,3,4]
arr2 = [2,2,3,3]
# arr1 = [4]
# arr2 = [5]
ret_val = get_intersection(arr1, arr2)
if ret_val:
    print(ret_val)
else:
    print(-1)
'''

def get_intersection(arr1, arr2):
    i = 0 
    while i < len(arr1):
        j = 0 
        while j < len(arr2):
            if arr1[i] == arr2[j]:
                print(arr1[i])
                del arr2[j] 
            j+=1
        i+=1
arr1 = [1,2,2,2,3,4]

arr2 = [2,2,3,3]


ret_val = get_intersection(arr1, arr2)
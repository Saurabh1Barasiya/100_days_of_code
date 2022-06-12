# find unique element in a array.
'''
arr = [1,1,1,2,2,2,3,4,5]
for i in arr:
    if arr.count(i) == 1:
        print(i)
'''


def count(val,arr):
    c = 0
    for i in arr:
        if i==val:
            c+=1
    return c 

def getUniqueElements(arr):
    for i in arr:
        if count(i,arr) == 1:
            print(i)

arr = [1,1,1,2,2,2,3,3,4,5]
getUniqueElements(arr)
# get sum of a array.

# arr = [1,2,3,4,5]
# addtion = 0
# for i in arr:
#     addtion += i
# print(addtion)

def getSum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + getSum(arr[1:])
ans = getSum([1,2,3,4,5])
print(ans)




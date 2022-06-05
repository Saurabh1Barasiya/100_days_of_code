# check weather array is sorted or not.
'''
arr = [2,0,6,8,10]
i = 0
while i < len(arr)-1:
    if arr[i] > arr[i+1]:
        print("not sorted")
        break
    i += 1
else:
    print("sorted")
'''

def isSorted(arr):
    print("arr: ", arr)
    if len(arr) == 0 or len(arr) == 1:
        return True
    if arr[0]> arr[1]:
        return False
    # del arr[0]
    # return isSorted(arr)
    return isSorted(arr[1:])

ans = isSorted([2,4,6,8,10])
# print(ans)
if ans:
    print(f"Array is sorted",ans)
else:
    print(f"Array is not sorted",ans)
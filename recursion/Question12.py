# Binary Search using recursion.


def binary_search(array,element,start,end):
    if start > end:
        return f"Element {element} not found in the array"
    mid = (start + end)//2
    if array[mid] == element:
        return f"Element {element} found at index {mid}"
    elif element > array[mid]:
        start = mid + 1
        return binary_search(array,element,start,end)
    else:
        end = mid - 1
        return binary_search(array,element,start,end)

array=[1,2,3,4,5,6,7,8]
element=1
ans=binary_search(array,element,0,7)
print(ans)
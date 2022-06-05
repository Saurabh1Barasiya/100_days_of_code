def Binary_search(array,element):
    start = 0 
    end = len(array) - 1
    # mid = (start + end)//2
    mid = start+(end-start)//2  # This is the same as the above line, when number is very big.
    while start <= end:
        if array[mid] == element:
            return f"Element {element} found at  index {mid}"
        elif element > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = start+(end-start)//2 # when number is very big.
    else:
        return f"Element {element} not found in the array"

array = [2,4,5,6,7,8,9,10,11,12]
element = 100

ans = Binary_search(array,element)
print(ans)

# worst case time complexcity O(Log n)
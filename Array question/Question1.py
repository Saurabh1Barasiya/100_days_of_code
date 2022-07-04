# reverse an Array.
# arr = [1,2,3,4,5,6]
# print(arr[::-1])
# print(arr)
# arr.reverse()
# print(arr)

arr = [10,20,30,40,50,60]
print("Before sortinng array " ,arr)
start = 0
end = len(arr)-1
while start < end:
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
print("After sortinng array   ",arr)

# time complexity is O(n/2)
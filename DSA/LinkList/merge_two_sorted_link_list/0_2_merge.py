# divide.


# ye intire array ko single array me convert kar dega.

def divide(arr):
    if len(arr) == 1:
        print(arr,end=" ")
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    divide(left)
    divide(right)

arr = [5,6,2,1,0]
divide(arr)

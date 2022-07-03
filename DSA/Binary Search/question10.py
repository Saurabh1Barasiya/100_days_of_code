# The painter’s partition problem.

def is_possible(arr,mid,m):
    i = 0
    painter = 1
    paint_sum = 0
    while i < len(arr):
        if arr[i] + paint_sum <= mid:
            paint_sum += arr[i]
        else:
            painter += 1
            paint_sum = arr[i]
            if painter > m or arr[i] > mid:
                return False
        i += 1
    return True

def binary_search(arr,m):
    start = 0
    end = sum(arr)
    mid = (start + end) // 2
    ans = 0
    while start <= end:
        if is_possible(arr, mid,m):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return ans

# arr = [10, 10, 10, 10]
# arr = [5,5,5,5]
# arr = [10,20,30,40]
# m = 2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 3
ans = binary_search(arr,m)
print(ans)


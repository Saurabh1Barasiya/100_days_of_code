# Book allocation problem using  binary search.

def is_possible(arr,mid,m):
    student_count = 1
    pages_sum = 0
    i = 0
    while i < len(arr):
        if arr[i] + pages_sum < mid:
            pages_sum += arr[i]
        else:
            student_count += 1
            if student_count > m or arr[i] > mid:
                return False
            pages_sum = arr[i]
        i += 1
    return True

def binary_search_book_allocation(arr,s,m):
    start = s
    end = sum(arr)
    mid = start + (end-start)//2
    while start < end:
        print(start,end)
        if is_possible(arr,mid,m):
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
        mid = start + (end-start)//2
        print("mid is ",mid)
    return ans

arr = [10,20,30,40]
m = 2
s = 0
val = binary_search_book_allocation(arr,s,m)
print("Final answer",val)

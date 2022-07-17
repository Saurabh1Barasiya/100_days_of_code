# check array is array or not using recursion.

def is_sorted(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        return is_sorted(arr[1::])

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    ans = is_sorted(array)
    print(ans)
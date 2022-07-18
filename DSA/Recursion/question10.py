# reverse string using recursion method 2.
def array_reverse_recursion(arr,start,end):
    # base case.
    if start > end:
        return
    # recursive case.
    else:
        arr[start],arr[end] = arr[end],arr[start]
        array_reverse_recursion(arr,start+1,end-1)
        return arr
if __name__ == '__main__':
    string_arr = list("ABCDEF")
    start = 0
    end = len(string_arr)-1
    ans = ''.join(array_reverse_recursion(string_arr,start,end))
    print(ans)

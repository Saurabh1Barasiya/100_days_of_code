# reverse of an array using recursion.

def array_reverse_recursion(arr):
    # base case.
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    # recursive case.
    else:
        return list(arr[-1])+array_reverse_recursion(arr[:len(arr)-1:])
if __name__ == '__main__':
    
    # string_arr = ["A","B","C","D","E","F"]
    string_arr = list("ABCDEF")
    ans = array_reverse_recursion(string_arr)
    ans = ''.join(ans)
    print(ans)



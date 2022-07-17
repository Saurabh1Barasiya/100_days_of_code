# linear search using recursion. 
def linear_search_recursion(arr,key):
    if len(arr) == 0:
        return False
    if arr[0] == key:
        return True
    else:
        return linear_search_recursion(arr[1::],key)

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    ans = linear_search_recursion(array,1)
    print(ans)
    
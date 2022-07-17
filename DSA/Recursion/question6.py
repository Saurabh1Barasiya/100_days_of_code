# getsum of array using recursion. 
def get_sum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+get_sum(arr[1::])

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    ans = get_sum(array)
    print(ans)
    
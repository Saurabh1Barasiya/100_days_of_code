# Amazone Question .

def solve(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        return arr[0] + solve(arr[1:])


if __name__ == '__main__':
    arr = [4, 5, 6, 7]
    ans = solve(arr)
    print(ans)
    print(ans%10) # print last digit.

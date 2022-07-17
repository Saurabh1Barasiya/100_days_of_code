# get power  using recursion.
def get_power(num,n):
    if n == 0:
        return 1
    else:
        return num * get_power(num,n-1)

if __name__ == "__main__":
    ans = get_power(3, 3)
    print(ans)
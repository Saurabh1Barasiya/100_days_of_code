# get_power a^b using recursion.

def get_power(a,b):
    if b == 0:
        return 1
    else:
        return a * get_power(a,b-1)

if __name__ == "__main__":
    a = int(input(""))
    b = int(input(""))
    ans = get_power(a,b)
    print(ans)
# calculate 2 to the power of n using recursion.

def calculate_power(n):
    if n == 0:
        return 1
    return 2 * calculate_power(n-1)

n = int(input("Enter power to calculate"))

print(calculate_power(n))

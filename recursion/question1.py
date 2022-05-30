#  print number 10 to 1 using recursion.

def print_numbers(n):
    if n == 0: 
        # base case..
        return
    print(n) # processing..
    print_numbers(n-1) # recursive call..

number = int(input("Enter a number : "))
print_numbers(number)

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
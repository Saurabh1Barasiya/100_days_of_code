def print_numbers(n):
    if n == 0: 
        # base case..
        return
    print_numbers(n-1) # recursive call..
    print(n) # processing..

number = int(input("Enter a number : "))
print_numbers(number)

# print_numbers(5)  n = 5
# print_numbers(4)  n = 4
# print_numbers(3)  n = 3
# print_numbers(2)  n = 2   
# print_numbers(1)  n = 1
# print_numbers(0)  return 

# 1 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10
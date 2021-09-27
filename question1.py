
 
# write a python program to using a function to print factroial number series from n to m numbers.

def fact_calculate(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
    return fact
    

n = int(input("Please enter firt number."))
m = int(input("Please enter secound number."))
for i in range(n,m+1):
    print(fact_calculate(i))
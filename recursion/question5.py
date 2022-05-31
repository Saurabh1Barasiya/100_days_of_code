# calculate factroil using recursion 

n=int(input("Enter number to calculate factroil.."))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(n))
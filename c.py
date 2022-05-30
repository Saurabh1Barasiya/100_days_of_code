# write a program that add two numbers
'''
def add(a, b):
    return a + b

print(add(1, 2))

# wite a program that subtract two numbers
def subtract(a, b):
    return a - b

print(subtract(1, 2))

# write a program that multiply two numbers
def multiply(a, b):
    return a * b

print(multiply(1, 2))

# write a program that divide two numbers
def divide(a, b):
    return a / b
print(divide(1, 2))

# write a program that take two numbers and return the remainder
def remainder(a, b):
    return a % b    
print(remainder(1, 2))

# write a program that take two numbers and return the power
def power(a, b):
    return a ** b
print(power(1, 2))

# write a program that take two numbers and return the square root
def square_root(a, b):
    return a ** (1/b)
print(square_root(1, 2))

# write a program that genrate fibonacci series of 10 numbers
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
print(fibonacci(10))
exit()
# '''
# super_herios = ["IronMen","captan meriaca","thor","hulk","black widow","spider"]
# print(super_herios[1])

d = {'a':5,'b':2,'c':3,'d':10,'e':1}
key=sorted(d.keys())
val = sorted(d.values(),reverse=True)
print(key)
print(val)
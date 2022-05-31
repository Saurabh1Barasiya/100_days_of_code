# def fibo(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fibo(n-1)+fibo(n-2)
# print(fibo(4))

def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n-1)+fibo(n-2)

for i in range(1,11):
    print(fibo(i))
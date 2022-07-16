# get gcd --> greatest common divisor // Heights common divisor HCF.


# def gcd(a,b):
#     maxi = a if a>b else b
#     for i in range(maxi,1,-1):
#         if a%i==0 and b%i==0:
#             return i


def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
    
ans = gcd(10,15)
print(ans)
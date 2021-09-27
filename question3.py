def demo(*value):
    prod = 1
    power = 0
    for i in range(1,11):
        prod = prod * i
        power = power + (i ** 2)
    print('The product of first 10 numbers : ',prod)
    print('The Power of first 10 numbers : ',power)

demo(1,2,3,4,5,6,7,8,9,10,11,12,13,14)
# 3628800

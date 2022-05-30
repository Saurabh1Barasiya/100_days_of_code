# fibinachi series useing generator.

def gen1(n):
    a = -1
    b = 1
    for i in range(n):
        c = a+b
        yield c
        # a = b
        # b = c
        a,b = b, c
for i in gen1(10):
    print(i)
# Problem Statement.
'''
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
'''

a = 3
b = 10
c = 4
d = 11
for i in range(1,6):
    for j in range(1,10):
        if j<=i:
            if i == 1:
                print(j,end="")
            else:
                if i % 2 == 0:
                    if i == 2:
                        print(a,end="")
                        a = a-1
                    elif i == 4:
                        print(b,end="")
                        b = b-1
                else:
                    if i == 3:
                        print(c,end="")
                        c = c+1
                    elif i == 5:
                        print(d,end="")
                        d = d + 1
                if i != j:
                    print("*",end="")
        else:
            print(" ",end="")
    print("")
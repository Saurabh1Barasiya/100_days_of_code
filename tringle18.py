for i in range(1,8):
    for  j in range(1,8):
        if i == j or j == (8-i):
            if i==j:
                print("\\",end=' ')
            else:
                print("/", end=' ')
        else:
            print(" ",end=' ')
    print("")


for i in range(1,8):
    for  j in range(1,8):
        if i == j or j == (8-i):
            if i==j:
                print("*",end=' ')
            else:
                print("*", end=' ')
        else:
            print(" ",end=' ')
    print("")

k = 7
for i in range(1,8):
    for  j in range(1,8):
        if i == j or j == (8-i):
            if i==j:
                print(i,end=' ')
            else:
                print(k, end=' ')
                k = k-1
        else:
            print(" ",end=' ')
    print("")



for i in range(1,8):
    for  j in range(1,8):
        if j == (8-i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("")
for i in range(1,8):
    for  j in range(1,8):
        if i == j:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("")
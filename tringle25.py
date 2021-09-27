# Problem Statement.
'''
1     
10    
101
1010
10101
101010
'''

for i in range(1,7):
    k = 1
    for j in range(1,7):
        if j<=i:
            print(k,end="")
            if k == 1:
                k = 0
            elif k == 0:
                k = 1
        else:
            print(" ",end="")
    print("")
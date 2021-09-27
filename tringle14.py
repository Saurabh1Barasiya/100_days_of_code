# Problem Statement.
'''
6543210
543210 
43210
3210
210
10
0
'''

for i in range(1,8):
    k = 7-i
    for j in range(1,8):
        if j>=1 and j<=(8-i):
            print(f"{k}",end=" ")
            k = k-1
        else: 
            print(" ",end=" ")
    print("")
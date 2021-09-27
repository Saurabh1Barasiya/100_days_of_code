# Problem Statement.
'''
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
'''

for i in range(5):
    m = 0
    for j in range(5):
        if j<=i:
            print(m,end="")
            m = m + i
        else:
            print(" ",end="")
    print("")
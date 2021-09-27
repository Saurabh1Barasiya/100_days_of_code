# Problem Statement.
'''
ABCDEFG
ABC EFG
AB   FG
A     G
'''

A = [0,"A","B","C","D","E","F","G"]
for i in range(1,5):
    for j in range(1,8):
        if j<=(5-i) or j>=(3+i):
            print(A[j],end="")
        else:
            print(" ",end="")
    print("")
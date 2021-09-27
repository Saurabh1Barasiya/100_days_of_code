# Problem Statement.
'''
A
BA
CBA
DCBA
'''
A = [0,'A','B','C','D']

for i in range(1,5):
    k = i         
    for j in range(1,5):
        if j<=i:
            if i == 1:
                print(A[k],end="")
            else:
                print(A[k],end="")
                k = k-1
        else:
                print("",end="")
    print("")
        
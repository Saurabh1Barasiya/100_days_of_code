# Problem Statement.
'''
   1   
  12A  
 123AB
1234ABC
'''

A = ["A","B","C"]
for i in range(1,5):
    k = 1
    m = 0
    for j in range(1,8):
        if j>=(5-i) and j<=(3+i):
            if j<=4:
                print(k,end="")
                k += 1
            else:
                print(A[m],end="")
                m += 1
        else:
            print(" ",end="")
    print("")
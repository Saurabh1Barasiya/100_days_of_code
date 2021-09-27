# Problem Statement.
'''
   A1
  AB12
 ABC123
ABCD1234
'''
A=[0,"A","B","C","D"]
for i in range(1,5):
    k = 1
    m = 1
    for j in range(1,9):
        if j>=(5-i) and j<=(4+i):
            if j <= 4:
                print(f"{A[k]}",end="")
                k += 1
            else:
                print(m, end="")
                m+=1
        else:
            print(" ",end="")
    print("")
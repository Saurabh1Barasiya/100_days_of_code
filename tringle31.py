# Problem Statement.
'''
    A
   CB
  FED
 JIHG
ONMLK
'''
A = [0,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
print(len(A))
sum = 0
for i in range(1,6):
    sum = sum + i
    c = sum 
    for j in range(1,6):
        if j>=(6-i):
            print(f"{A[c]}",end=" ")
            c = c-1
        else:
            print(" ",end=" ")
    print("")
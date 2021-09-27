# Problem statement.
'''
*******
 *****
  ***
   *
'''
for i in range(1,5):
    for j in range(1,8):
            if j>=i and j<=(8-i):
                print("*",end="")
            else:
                print(" ",end="")
    print("")
print("-"*25)


for i in range(1,5):
    for j in range(1,8):
            if j>=i and j<=(8-i):
                print(f"{i}",end="")
            else:
                print(" ",end="")
    print("")
print("-"*25)


for i in range(1,5):
    for j in range(1,8):
            if j>=i and j<=(8-i):
                print(f"{j}",end="")
            else:
                print(" ",end="")
    print("")
print("-"*25)

A = [0,'A','B','C','D','E','F','G']
for i in range(1,5):
    for j in range(1,8):
            if j>=i and j<=(8-i):
                print(f"{A[j]}",end=" ")
            else:
                print(" ",end=" ")
    print("")
print("-"*25)


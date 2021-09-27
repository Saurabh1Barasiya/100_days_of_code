# Problem statement.

'''
*
**
***
****
***
**
*
'''

for i in range(1,8):
    for j in range(1,5):
        if i<=4:
            if j>=1 and j<=i:
                print("*",end="")
            else:
                print("",end="")
        else:
            if j>=1 and j<=(8-i):
                print("*",end="")
            else:
                print("",end="")
    print("")

print("-"*25)


for i in range(1,8):
    for j in range(1,5):
        if i<=4:
            if j>=1 and j<=i:
                print(f"{i}",end="")
            else:
                print("",end="")
        else:
            if j>=1 and j<=(8-i):
                print(f"{i}",end="")
            else:
                print("",end="")
    print("")

print("-"*25)

for i in range(1,8):
    for j in range(1,5):
        if i<=4:
            if j>=1 and j<=i:
                print(f"{j}",end="")
            else:
                print("",end="")
        else:
            if j>=1 and j<=(8-i):
                print(f"{j}",end="")
            else:
                print("",end="")
    print("")

print("-"*25)

A = [0,'A','B','C','D']
for i in range(1,8):
    for j in range(1,5):
        if i<=4:
            if j>=1 and j<=i:
                print(f"{A[j]}",end=" ")
            else:
                print(" ",end=" ")
        else:
            if j>=1 and j<=(8-i):
                print(f"{A[j]}",end=" ")
            else:
                print(" ",end=" ")
    print("")
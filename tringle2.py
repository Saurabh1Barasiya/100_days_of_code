# Problem Statememt
'''
    *
   **
  *** 
 **** 
*****
'''

for i in range(1,6):
    for j in range(1,6):
        if j>=(6-i):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

print("------------------------------------------")

for i in range(1,6):
    for j in range(1,6):
        if j>=(6-i):
            print(i,end="")
        else:
            print(" ",end="")
    print("")
print("------------------------------------------")

for i in range(1,6):
    for j in range(1,6):
        if j>=(6-i):
            print(j,end="")
        else:
            print(" ",end="")
    print("")
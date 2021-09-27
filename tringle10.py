# Problem Statement.
'''
   *   
  ***  
 *****
*******
 *****
  ***
   *
'''
for i in range(1,8):
    for j in range(1,8):
        if i<=4:
            if j>=(5-i) and j<=(3+i):
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if j>=(i-3) and j<=(11-i):
                print("*",end="")
            else:
                print(" ",end="")
    print("")

print("-"*20)



for i in range(1,8):
    for j in range(1,8):
        if i<=4:
            if j>=(5-i) and j<=(3+i):
                print(f"{j}",end="")
            else:
                print(" ",end="")
        else:
            if j>=(i-3) and j<=(11-i):
                print(f"{j}",end="")
            else:
                print(" ",end="")
    print("")

print("-"*25)

for i in range(1,8):
    for j in range(1,8):
        if i<=4:
            if j>=(5-i) and j<=(3+i):
                print(f"{i}",end="")
            else:
                print(" ",end="")
        else:
            if j>=(i-3) and j<=(11-i):
                print(f"{i}",end="")
            else:
                print(" ",end="")
    print("")
# Problem Statement.
'''
* * * * * 
* * * *   
* * *
* *
*
'''
for i in range(1,6):
    for j in range(1,6):
        if j<=(6-i):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")

print("-"*20)

for i in range(1,6):
    for j in range(1,6):
        if j<=(6-i):
            print(f"{i} ",end="")
        else:
            print("  ",end="")
    print("")

print("-"*20)

for i in range(1,6):
    for j in range(1,6):
        if j<=(6-i):
            print(f"{j} ",end="")
        else:
            print("  ",end="")
    print("")
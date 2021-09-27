# problem statement.
A = ["A","B","C","D","E","F","G","H","I"]
for i in range(1,6):
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")
print("-"*25)
for i in range(1,6):
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i):
            print(f"{i} ",end="")
        else:
            print("  ",end="")
    print("")
print("-"*25)

for i in range(1,6):
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i):
            print(f"{j} ",end="")
        else:
            print("  ",end="")
    print("")
print("-"*25)

for i in range(0,5):
    for j in range(0,9):
        if j>=(6-i) and j<=(4+i):
            print(f"{A[j]} ",end="")
        else:
            print("  ",end="")
    print("")
print("-"*25)

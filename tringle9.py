# Problem Statement.
A = [0,'A','B','C','D',]
for i in range(1,5):
    k = 0
    for j in range(1,8):
        if j<=(5-i) or j>=(3+i):
            if j <= 4:
                k += 1
            else:
                if i >=2:
                    k +=1
                k = k- 1
            print(f"{A[k]}",end="")
        else:
            print(" ",end="")
    print("")
print("-"*25)


# Problem Statement.
'''

'''
for i in range(1,6):
    for j in range(1,9):
        if i <= 2:
            if j<=i:
                # print("*",end="")
                print(j,end="")
            else:
                print(" ",end="")
        else:
            if j<= i+i-2:
                print(j,end="")
            else:
                print(" ",end="")
    print("")
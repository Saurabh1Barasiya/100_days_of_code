# Problem Statement.
'''
*   *
 * * 
  *
 * *
*   *
'''
for i in range(1,6):
    for j in range(1,6):
        if (i == j) or (j==6-i):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
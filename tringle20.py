# Problem Statement.
'''
********* 
 *******  
  *****
   ***
    *
'''
for i in range(1,6):
    for j in range(1,11):
        if j>=i and j<=10-i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
# Problem statement.
''' 
* * * * * * * * * 
* * * *   * * * * 
* * *       * * *
* *           * *
*               * 
* *           * *
* * *       * * * 
* * * *   * * * *
* * * * * * * * *
'''
for i in range(1,10):
    for  j in range(1,10):
        if i<=5:
            if j<=(6-i) or j>=(4+i):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        else:
            if j<=(i-4) or j>=(14-i):
                print("*",end=' ')
            else:
                print(" ",end=' ')
        
    print("")
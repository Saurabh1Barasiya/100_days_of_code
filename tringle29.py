# Problem Statement.
'''
   1   
  212  
 32123
4321234
'''
for i in range(1,5):  
    a = i   
    for j in range(1,8):
        if j>=5-i and j<=3+i:
            if j<=4:
               print(a,end="") 
               a = a-1
            else: 
                if j==5:
                    a=a+1
                a = a+1
                print(a,end="")
        else:
            print(" ",end="")
    print("")
        
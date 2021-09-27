# Problem Statement.
for i in range(1,10):
    for j in range(1,6):
        if i <=3:
            if j>=(6-i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if j>=i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        
        if i>=5 and i<=7:
            if j<=(i-4):
                print("*",end="")
            else:
                print("",end="")
        else:
            if i>7:
                if j<=(10-i):
                    print("*",end="")
                else:
                    print("",end="")   
        if ( i == 4  or i == 5)  and (j==3):
            print("|",end="")
    print("")
            

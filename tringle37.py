# Problem Statement.
'''
1     
6 2    
10 7 3
13 11 8 4
15 14 12 9 5
'''

a = 5
k = 1    
m = 5
for i in range(1,6):
    p = k
    s = m 
    for j in range(1,6):
        if j<=i:
            print(p,end=" ") 
            p = p-s
            s = s+1
        else:
            print("",end=" ")
    print("")
    k= k+a
    a=a-1
    m = m-1

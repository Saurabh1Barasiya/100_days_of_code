# Problem Statement.
'''
   1   
  A B  
 1 2 3 
A B C D
'''
num = [1,2,3]
alp = ["A", "B", "C", "D"]
for i in range(1,5):
    a = 0
    m  = 0
    flag = True
    for  j in range(1,8):
        if j>=5-i and j<= 3+i and flag:
            if i % 2 == 0:
                print(alp[a],end="")
                a = a+1
                flag = False
            else:
                print(num[m],end="")
                m+=1
                flag = False
        else:
            print(" ", end="")
            flag = True
    print("")



# Problem Statement.

'''
        1 
      1 2 
    1 2 3
  1 2 3 4
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''





# d = {1:5,2:4,3:3,4:2,5:1}
# for i in range(1,10):
#     for j in range(1,6):
#         if i <= 5:
#             if j>=(6-i):
#                 print(d[j],end=" ")
#             else: 
#                 print(" ",end=" ")
#         else:
#             if j>=(i-4):
#                 print(d[j],end=" ")
#             else: 
#                 print(" ",end=" ")
#     print("")




for i in range(1,10):
    k = 1
    for j in range(1,6):
        if i <= 5:
            if j>=(6-i):
                print(k,end=" ")
                k+=1
            else: 
                print(" ",end=" ")
        else:
            if j>=(i-4):
                print(k,end=" ")
                k+=1
            else: 
                print(" ",end=" ")
    print("")


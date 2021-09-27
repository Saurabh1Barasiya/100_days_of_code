# Problem statement.
'''
   1   
  232  
 34543 
4567654
'''
# for i in range(1,5):
#     k = i   
#     k = k-1      
#     for j in range(1,8):
#             if j>=(5-i) and j<=(3+i):
#                 if i == 1:
#                     k = 1
#                 else:
#                     if j<=4:
#                         k = k+1
#                     else:
#                         k = k-1
#                 print(f"{k}",end="")
#             else:
#                 print(" ",end="")

#     print("")
# print("-"*25)


# More simpler version.

for i in range(1,5):
    k = i   
    k = k-1      
    for j in range(1,8):
            if j>=(5-i) and j<=(3+i):
                    if j<=4:
                        k = k+1
                    else:
                        k = k-1
                    print(f"{k}",end="")
            else:
                print(" ",end="")
    print("")
print("-"*25)





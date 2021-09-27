# Problem Statement.
'''
    *    
   * *   
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    k = True
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i) and k:
            print("*",end="")
            k = False
        else:
            print(" ",end="")
            k = True
    print("")
print("-"*25)


for i in range(1,6):
    k = True
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i) and k:
            print(f"{i}",end="")
            k = False
        else:
            print(" ",end="")
            k = True
    print("")
print("-"*25)

for i in range(1,6):
    k = True
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i) and k:
            print(f"{j}",end="")
            k = False
        else:
            print(" ",end="")
            k = True
    print("")
print("-"*25)

A = ["A","B","C","D","E","F","G","H","I"] 
for i in range(1,6):
    k = True
    for j in range(1,10):
        if j>=(6-i) and j<=(4+i) and k:
            print(f"{A[i]}",end="")
            k = False
        else:
            print(" ",end="")
            k = True
    print("")
print("-"*25)

# A = ["A","B","C","D","E","F","G","H","I"] 
# for i in range(0,5):
#     k = True
#     for j in range(0,9):
#         if j>=(5-i) and j<=(3+i) and k:
#             print(f"{A[j]}",end="")
#             k = False
#         else:
#             print(" ",end="")
#             k = True
#     print("")
# print("-"*25)


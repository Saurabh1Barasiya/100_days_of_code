for i in range(1,6):
    for j in range(1,6):
        if j == i or j == (6-i):
            print(j,end='')
        else:
            print(' ',end='')
    print('')



# for i in range(1,8):
#     for  j in range(1,8):
#         if i == j:
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print("")
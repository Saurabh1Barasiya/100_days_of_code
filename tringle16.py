# Problem statement.
'''
\*****/
*\***/*
**\*/**
***\***
**/*\**
*/***\*
/*****\

'''

for i in range(1,8):
    for  j in range(1,8):
        if i == j or j == (8-i):
            if i==j:
                print("\\",end='')
            else:
                print("/", end='')
        else:
            print("*",end='')
    print("")
a = [0,5,4,3,5,4]
b = [0,1,2,3,1,2]
for i in range(1,6):
    for j in range(1,6):
        if j == i:
            print(a[j],end='')
        else:
            print(' ',end='')
        if j == (6-i):
            if j == 3:
                pass
            else:
                print(b[j],end='')
        else:
            print(' ',end='')
    print('')

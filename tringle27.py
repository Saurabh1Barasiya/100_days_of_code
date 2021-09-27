# Problem Statement.

'''
                    0
                  1 2 1
                2 3 4 3 2
              3 4 5 6 5 4 3
            4 5 6 7 8 7 6 5 4
          5 6 7 8 9 0 9 8 7 6 5
        6 7 8 9 0 1 2 1 0 9 8 7 6
      7 8 9 0 1 2 3 4 3 2 1 0 9 8 7
    8 9 0 1 2 3 4 5 6 5 4 3 2 1 0 9 8
  9 0 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 0 9
0 1 2 3 4 5 6 7 8 9 0 9 8 7 6 5 4 3 2 1 0
  9 0 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 0 9
    8 9 0 1 2 3 4 5 6 5 4 3 2 1 0 9 8
      7 8 9 0 1 2 3 4 3 2 1 0 9 8 7
        6 7 8 9 0 1 2 1 0 9 8 7 6
          5 6 7 8 9 0 9 8 7 6 5
            4 5 6 7 8 7 6 5 4
              3 4 5 6 5 4 3
                2 3 4 3 2
                  1 2 1
                    0
'''

n = 19
k = 20
for i in range(1,22):
    m = i-1-1
    o = k
    for j in range(1,22):
        if i<=11: 
            if j>=12-i and j<=10+i:
                if j<=11:
                    if i == 1:
                        m = 0
                    else:
                        m = m+1
                else:
                    m = m-1
                print(m%10,end=" ")
            else:
                print(" ",end=" ")
        else:
            if j>= i-10 and j<=32-i:
                if j<=11:
                    print(o%10,end=" ")
                    o = o+1
                else:
                    if j == 12:
                        o = o-1
                    o = o-1
                    print(o%10,end=" ")
                
            else:
                print(" ",end=" ")
    k = k-1
    print("")


'''
arr = [
    [1, 2 ,3],
    [4, 5, 6],
    [9, 8, 9]
]
find_l = []
find_r = [] 
k = 2
for i in range(0,3):
    for j in range(0,3) :
        if i == j:
           find_l.append(arr[i][j])
        if k == j:
           find_r.append(arr[i][j])
           k-=1 
    print("")
print(abs(sum(find_l)-sum(find_r)))
print(find_r)
print(find_l)
'''

def diagonalDifference(arr):
    find_l = []
    find_r = [] 
    k = 2
    for i in range(0,3):
        for j in range(0,3) :
            if i == j:
               find_l.append(arr[i][j])
            if k == j:
                find_r.append(arr[i][j])
                k-=1 
        print("")
    return abs(sum(find_l)-sum(find_r))


arr = [
    [1, 2 ,3],
    [4, 5, 6],
    [9, 8, 9]
]

print(diagonalDifference(arr))

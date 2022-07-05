# Move all zeros to right positions.
def move(arr):
    '''
    Its my approach.
    '''
    l1 = []
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] != 0:
            l1.append(arr[i])
        else:
            count += 1
        i+=1

    for i in range(count):
        l1.append(0)
    return l1
#arr = [0,1,0,3,12]
arr = [0,0,1,2]
ans = move(arr)
print(ans)


def calculate_both_digonal_absolute_value(arr):
    l1 = []
    l2 = []
    i = 0
    while i<3:
        j = 0
        while j<3:
            if j == i:
                l1.append(arr[i][j]) 
            if j == (2-i):
                l2.append(arr[i][j])
            j+=1
        i+=1
    res1 = sum(l1)
    res2 = sum(l2)
    return abs(res1-res2)



arr = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]
print(calculate_both_digonal_absolute_value(arr))



'''
def calculate_both_digonal_absolute_value(arr,n):
    l1 = []
    l2 = []
    i = 0
    while i<n:
        j = 0
        while j<n:
            if j == i:
                l1.append(arr[i][j]) 
            if j == ((n-1)-i):
                l2.append(arr[i][j])
            j+=1
        i+=1
    res1 = sum(l1)
    res2 = sum(l2)
    return abs(res1-res2)

    # n = user input size
    # arr = user input array
print(calculate_both_digonal_absolute_value(arr,n))

'''
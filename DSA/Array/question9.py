# find two same element.
def get_two(arr):
    l2 = []
    for i in arr:
        if arr.count(i) == 2:
           l2.append(i)
    return list(set(l2))
arr = [1,2,3,3,4,4,5,5]
print(get_two(arr))  

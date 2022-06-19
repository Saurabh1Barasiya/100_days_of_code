# [0, 0, 0, 1, 1, 1]
# get zeros first and ones last .

def diffrencieat(arr):
    zeros = []
    ones = []
    for i in arr:
        zeros.append(i) if i == 0 else ones.append(i)
    return zeros+ones
arr = [0,1,1,0,0,1]
print(diffrencieat(arr))

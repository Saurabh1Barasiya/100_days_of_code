# Apple google Most Important Question.

def get_unique(counts):
    # print(counts,set(counts))
    return len(counts) == len(set(counts))

def find_unique(arr):
    counts = []
    unique=set(arr)
    for i in unique:
        counts.append(arr.count(i))
    return get_unique(counts)
arr = [1,2,2,2,1,3,1,1]
# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# arr = [1,2]
print(find_unique(arr))
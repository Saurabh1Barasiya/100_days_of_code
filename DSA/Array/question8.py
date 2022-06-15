# find single duplicate value in a array.
def find_duplicate_value(arr):
    for i in arr:
        if arr.count(i)==2:
          return i
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,14]
print(find_duplicate_value(arr))
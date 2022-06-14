# Sum of all elements in a array.
def get_sum(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum
arr = [1,2,3,4,5,6,7,8,9]
print(get_sum(arr))
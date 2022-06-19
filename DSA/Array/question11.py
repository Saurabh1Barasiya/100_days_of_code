# get pair sums.
def pair_sum(arr,s):
    l1 = []
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            ans = arr[i]+arr[j]
            if ans == s:
                l1.append(sorted((arr[i],arr[j])))
            j+=1
        i+=1
    return l1
# arr = [1,2,3,4,5]
arr = [2,-3,3,3,-2]
s = 0
print(pair_sum(arr,s))

# get pair sums tripplet.
def pair_sum_tripplet(arr,s):
    l1 = []
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            k = i + 2
            while k < len(arr):
                ans = arr[i]+arr[j]+arr[k]
                if ans == s:
                    l1.append(sorted((arr[i],arr[j],arr[k]))) 
                k+=1
            j+=1
        i+=1
    return l1
arr = [1,2,3,4,5]
s = 12
print(pair_sum_tripplet(arr,s))

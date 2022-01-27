from collections import Counter
n = int(input())
nums = list(map(int,input().strip().split()))[:n] 
customer = int(input())
bil = 0
d = Counter(nums)
for i in range(customer): 
    size,price = list(map(int,input().split()))
    if size in d.keys():
        if d[size] == 0:
            print(f'Size 6 no longer available, so no purchase.')
        else:   
            d[size] -= 1
            bil += price
print(f"totel money earned: {bil}") 



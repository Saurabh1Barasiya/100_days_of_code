from itertools import permutations
s,k = input().split(" ")
s = s.upper()
k = int(k)
per = list(permutations(s,k))
per.sort()
for i in per:
    print("".join(i))
   

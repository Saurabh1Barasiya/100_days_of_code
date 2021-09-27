


m = [1,2,3,4,5,6,7]
i = 0
l = []
mid =  len(m)//2
while i < mid:
    l.append(m[6-i])
    l.append(m[i])
    i = i + 1
l.append(m[mid])
for i in l:
    print(i,end="")

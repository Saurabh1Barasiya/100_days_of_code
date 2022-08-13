l1 = [2,3,5,7,9]
l2 = [1,4,6,8,10,11,12,13]

l3 = []

i = j = 0  # index
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1

# print(i,j)
while i < len(l1):
    print("not in")
    l3.append(l1[i])
    i += 1

while j < len(l2):
    l3.append(l2[j])
    j += 1

print(l3)
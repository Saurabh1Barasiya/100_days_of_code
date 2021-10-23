# input section.
n = int(input())
l = []
for _ in range(n):
    l.append(input())

# making list and set.
l = list(map(int, l))
s = set(l)

# make dictionary 
d = {}
for i in s:
    d.update({i:l.count(i)})


# actual logic

minimum = min(d.values())
maximum = max(d.values())


minimum_key = 0           
maximum_key = 0
for key, value in d.items():
    if value == minimum:
        minimum_key = key
    if value == maximum:
        maximum_key = key

if maximum_key > minimum_key:
    print(maximum-minimum)
else:
    del d[maximum_key]
    print(max(d.values()) - min(d.values()))


# simpe one

'''
s = "pppaabbbb"
l = ['a','b','p']
l1 = []
for i in l:
    l1.append(i)
    l1.append(str(s.count(i)))
print(''.join(l1))
'''



# secound  level
'''
l1 = []
s = "pppaabbbb"
print(sorted(s))
for i in sorted(s):
    if i not in l1:
        l1.append(i)
print(l1)
'''


# pythonic way

# output ----> a2b4p3
l1 = []
l2 = []
s  = "pppaabbbb"
[l1.append(i) for i in sorted(s) if  i not in l1]
for i in l1:
    l2.append(i)
    l2.append(str(s.count(i)))
print(''.join(l2))

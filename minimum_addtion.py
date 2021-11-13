'''
# User Input.
s = "4325"
s = '867'
'''

#  ---- main logic ------ 

s = "4325"
# s = '867'
final = []
if len(s) == 4:
    # first case.
    p1 = s[0:2]
    p2 = s[2:]
    r1 = int(p1)+int(p2)
    final.append(r1)
    # secound case.
    # consider p1
    a,b = p1
    final.append(int(''.join([b,a]))+int(p2))
    # third case.
    a,b = p2
    final.append(int(''.join([b,a]))+int(p1))
    # case four
    # change  p1 and p2 also.
    a,b = p1
    n,m = p2
    final.append(int(''.join([b,a])) + int(''.join([m,n])))
else:
    s = '867'
    l1 = list(s)
    print(l1)
    # first case.
    a = int(l1[0])
    b = int(''.join(l1[1:]))
    final.append(a+b)
    # secound case.
    a = int(l1[2])
    b = int(''.join(l1[0:2]))
    final.append(a+b)
    # third case.
    a = l1.pop(1)
    a = int(a)
    final.append(int(''.join(l1))+a)
print(min(final))
# minimun addtion

# Program for array rotation
# 1,2,3,4,5,6,7 
# 3,4,5,6,7,1,2     




l = [1,2,3,4,5,6,7]
k = 0
for i in range(0,2):
    l.append(l.pop(k))
print(l)
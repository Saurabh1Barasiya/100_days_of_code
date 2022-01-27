# import math
# r=int(input(""))
# if r>=20 and r<=30:
#     r = r*r
#     print(round(math.pi*r,2))
# else:
#     print("Wrong Radius Entry")

s = 'abcdefghijklmnopqrstuvwxyz'
a=input()
l=list(s)
l.reverse()
last_index = len(a)-1

start_index = s.index(a[0])
print(''.join(l[start_index:last_index+1]))
   
    



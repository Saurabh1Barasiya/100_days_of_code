x = 'Ter38'
f = []
rem_int = []

for i in x:
    if i.isalpha():
       f.append(chr(ord(i)+4))
       
for i in x:
    if not i.isalpha():
        rem_int.append(int(i)+4)   

for i in rem_int:
    f.append(str(i)) if i<= 9 else f.append(str(i//6))
            
print(''.join(f))
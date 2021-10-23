s = "ThisIsAngular"
# output ----->   this_is_angular
a = s[0].lower()
l = []
i = 1
while i < len(s):
    if s[i].isupper():
        l.append(a.lower()) 
        a = ''  
    a += s[i]
    i += 1
l.append(a.lower())
print('_'.join(l))
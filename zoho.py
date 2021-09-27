s = "a1b2c3"
s = "d2f4c6"
i = 0
while i < len(s):
    print(s[i]*int(s[i+1]),end='')
    i +=2
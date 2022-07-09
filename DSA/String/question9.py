# add extra character @40 after space in the string.

def add_extra_char(string):
    string = string.replace(" "," @40")
    return string
s1 = "My name is khan"
ans = add_extra_char(s1)
print(ans)
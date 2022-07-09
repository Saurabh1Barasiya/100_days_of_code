# Cheack palindrom with remove extra spaces.
def chek_palindrom(s):
    start = 0
    end = len(s)-1
    # case sensitivity ko ignore karna tha isiliye .lower() ka use kiya.
    while start <= end :
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    else:
        return True
    
def remove_extra_symbol(s):
    new_string = ""
    for i in s:
        if i.isalnum():
            new_string += i
    ans = chek_palindrom(new_string)
    return ans

# s = "321Noon123  %^&$"
s = "5?36@6?35"
print(remove_extra_symbol(s))

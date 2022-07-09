# Cheack palindrom with remove extra spaces. and ignore extra spaces.
def chek_palindrom(s):
    start = 0
    end = len(s)-1
    # case sensitivity ko ignore karna tha isiliye .lower() ka use kiya.
    while start <= end :
        if s[start] != s[end]:
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
    new_string = new_string.lower()
    ans = chek_palindrom(new_string)
    return ans

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    # s = ", "
    # s = "race a car"
    ans = remove_extra_symbol(s)
    print(ans)
def make_dictrinary(string):
    d = {}
    s = set(string)
    for chr in s:
        d[chr] = string.count(chr)
    return d

def get_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    d1 = make_dictrinary(str1)
    d2 = make_dictrinary(str2)

    for i in str1:
        if d1[i] != d2[i]:
            return False
    else:
        return True

# def get_anagrams(str1, str2):
#     if sorted(str1) != sorted(str2):
#         return False
#     else:
#         return True

if __name__ == '__main__':
    str1="listen"
    str2="silent"
 
    ans = get_anagrams(str1, str2)
    print(ans)

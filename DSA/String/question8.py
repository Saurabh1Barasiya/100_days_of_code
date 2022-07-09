# find maximum character count.

def get_max_character(s):
    letter = ''
    max_ = 0
    s1 = set(s)
    for i in s1:
        if s.count(i) > max_:
            letter = i
            max_ = s.count(i)
    return letter
if __name__ == '__main__':
    s = "teeeest"
    ans = get_max_character(s)
    print(ans)

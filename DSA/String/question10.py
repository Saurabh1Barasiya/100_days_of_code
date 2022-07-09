# Remove all Occurrences of a substring.
def get_min_string(string,part):
    if part not in string:
        return string
    else:
        new_string = ""
        a = string.find(part)
        b = a + len(part)-1
        i = 0
        while i < len(string):
            if i >= a and i <= b:
                pass
            else:
                new_string += string[i]
            i += 1
        #print(new_string)
        return get_min_string(new_string,part)
if __name__ == '__main__':
    s = "daabcbaabcbc"
    part = "abc"
    #s = "axxxxyyyyb"
    #s = "axxyyb"
    #part = "xy"
    ans = get_min_string(s, part)
    #print("---------------------------------")
    print(ans)


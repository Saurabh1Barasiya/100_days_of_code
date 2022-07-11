# Remove duplicate Occurrences from a string .

# aaa -- >  ""
# aaabbbc -- > c 
# aaabbdbccc -- > db

def isValid(s):
    check = False
    for i in s:
        if s.count(i) == 1:
            check = True
        else:
            check = False
            break
    if check:
        return True
    else:
        return False
# -----------------------------------------

def remove_duplicates(s):
    if len(s) == 0:
        return ""
    if isValid(s):
        return s
    else:
        original_string = s
        new_string = ""
        i = 0 
        flag = False   
        while i < len(original_string)-1:
            if original_string[i] == original_string[i+1]:
                flag = True
                i+=1
                continue
            if flag:
                new_string += original_string[i+1::]
                break
            else:
                new_string += original_string[i]
            i+=1
        else:
            if len(new_string) > 1:
                if original_string[i] != original_string[i-1]:
                    new_string += original_string[i]
            
    return remove_duplicates(new_string)
    
if __name__ == '__main__':
    # ans = remove_duplicates("aabbbcccc")
    # ans = remove_duplicates("saasbh")
    # ans = remove_duplicates("aaa")
    ans = remove_duplicates("aaabbdbccc")
    print(ans)
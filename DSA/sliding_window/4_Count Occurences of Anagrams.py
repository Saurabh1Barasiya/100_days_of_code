# Count Occurences of Anagrams.

# TC ---> O(n)
# SC ---> O(k)

def make_dictrinary(string):
    d = {}
    for i in string:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def search(pat, txt): 
    n = len(txt)
    k = len(pat)
    
    d = make_dictrinary(pat)
    
    length = len(d)
    
    # window size ==  j-i+1
    ans = 0
    
    i=0
    j=0
    
    while j < n:
        if txt[j] in d:
            d[txt[j]] -= 1
            if d[txt[j]] == 0:
                length -= 1
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            if length == 0:
                ans += 1
                   
            if txt[i] in d:
                d[txt[i]] +=1
                if d[txt[i]] == 1:
                    length += 1
            i+=1
            j+=1
    return ans

if __name__ == "__main__":
    txt = "forxxorfxdofr"
    pat = "for"
    res = search(pat, txt)
    print(res)

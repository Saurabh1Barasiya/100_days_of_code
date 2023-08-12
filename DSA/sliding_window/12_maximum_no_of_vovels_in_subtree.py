def check_vovels(ch):
    return (ch == 'a') or (ch == 'e') or (ch  == 'i') or (ch == 'o')  or (ch == 'u')

def maxVowels(s, k):
    i = j = maxv = count = 0
    n = len(s)
    while j < n:
        if check_vovels(s[j]):
            count += 1
        if j-i+1 == k:
            maxv = max(maxv,count)
            if check_vovels(s[i]):
                count -= 1
            i += 1
        j+=1
    return maxv
        

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    ans = maxVowels(s, k)
    print(ans)
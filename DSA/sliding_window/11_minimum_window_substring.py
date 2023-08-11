import sys

def mini_window(string, pattern):
    # first create a map for pattern.
    mp = {}
    for ch in pattern:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] = 1
    
    i = j = 0
    min_window_size = sys.maxsize
    min_start = 0
    required_count = len(pattern)
    n = len(string)

    while j < n:
        if string[j] in mp and mp[string[j]] > 0:
            required_count -= 1
        
        if string[j] in mp:
            mp[string[j]] -= 1

        while required_count == 0:
            if min_window_size > j-i+1:
                min_window_size = j-i+1
                min_start = i
            
            if string[i] in mp:
                mp[string[i]] += 1
                if mp[string[i]] > 0:
                    required_count += 1
            i+=1
        j+=1
    
    if min_window_size == sys.maxsize:
        return ""
    else:
        return string[min_start:min_start+min_window_size]
        



    
if __name__ == '__main__':
    string = "geeksforgeeks"
    pattern = "ork"
    ans = mini_window(string, pattern)
    print(ans)
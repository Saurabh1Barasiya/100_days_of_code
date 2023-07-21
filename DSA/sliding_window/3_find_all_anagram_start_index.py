# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# Find All Anagrams in a String.

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".



# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
class Solution:
    def get_indexces(self,s,p,k,n,ana):
        ans = []
        # process first window size.
        if ana == sorted(s[:k]):
            ans.append(0)
        
        # process rest of the part using sliding window.
        i = 1
        j = k
        while j < n:
            if ana == sorted(s[i:j+1]):
                ans.append(i)
            i+=1
            j+=1
        return ans

    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ana = sorted(p)
        n  = len(s)
        return self.get_indexces(s,p,k,n,ana)

'''

def get_indexces(s,k,n,ana):
    ans = []
    # process first window size.
    if ana == sorted(s[:k]):
        ans.append(0)
    
    # process rest of the part using sliding window.
    i = 1
    j = k
    while j < n:
        if ana == sorted(s[i:j+1]):
            ans.append(i)
        i+=1
        j+=1
    return ans



def findAnagrams(s, p):
    k = len(p)  
    ana = sorted(p)
    n  = len(s)
    return get_indexces(s,k,n,ana)



if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
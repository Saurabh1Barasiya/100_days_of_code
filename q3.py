class Solution:
    def isSumString (ob,S, idx=0, val1=None, val2=None, cnt=0):
        # code here 
        if idx==len(S):
            return True if cnt>2 else False
        if val1==None:
            tmp=''
            for i in range(idx, len(S)//3+1):
                tmp+=S[i]
                if ob.isSumString(S, i+1, tmp, val2, cnt+1):
                    return True
            return False
        elif val2==None:
            tmp=''
            for i in range(idx, len(S)-1):
                tmp+=S[i]
                if ob.isSumString(S, i+1, val1, tmp, cnt+1):
                    return True
            return False
        else:
            req=str(int(val1)+int(val2))
            if idx+len(req)<=len(S):
                new=S[idx: idx+len(req)]
                if new==req and ob.isSumString(S, idx+len(req), val2, new, cnt+1):
                    return True
            return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
# } Driver Code Ends
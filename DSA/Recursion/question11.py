# check string is palindrome or not using recursion.

def chek_palindrome(string,start,end):
    # base case.
    print(string)
    if start > end:
        return True
    
    if string[start] != string[end]:
        return False

    return chek_palindrome(string,start+1,end-1)

if __name__ == '__main__':
    string = "NAMAN"
    start = 0
    end = len(string)-1
    ans = chek_palindrome(string,start,end)
    print(ans)
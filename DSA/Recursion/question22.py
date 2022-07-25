# permutation of a string or array.
# abc -> abc, acb, bac, bca, cab, cba.

def permutation(string,ans,index):
    # base case.
    if index >= len(string):
        ans.append(''.join(string))
        return
    
    # recursive case.
    j = index
    while j < len(string):
        string[index],string[j] = string[j],string[index] # swap.
        permutation(string,ans,index+1)   # recursive call.
        string[index],string[j] = string[j],string[index] # swap back.
        j += 1

if __name__ == '__main__':
    ans = []
    string = list("abc")
    index = 0
    permutation(string,ans,index)
    print(ans)
    print(len(ans))

    # ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
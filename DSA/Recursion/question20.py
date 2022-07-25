# subsequences of a string.
# abc = [['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]

def subsequences(string,index,output,ans):
    if index >= len(string):
        if len(output) > 0:
            ans.append(output)
        # ans.append(output)
        return
    
    # exclude wali call.
    subsequences(string,index+1,output.copy(),ans)

    # include wali call.
    element = string[index]
    output.append(element)
    subsequences(string,index+1,output.copy(),ans)
    


if __name__ == '__main__':
    string = "abc"
    index = 0
    output = []
    ans = []
    subsequences(string,index,output,ans)

    print(ans)


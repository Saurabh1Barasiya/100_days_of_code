# phone keybord problem. 
# letter combinations of a number.
# most imp question.

def solve(digit,index,output,mapping,ans):
    # base case.
    if index >= len(digit):
        ans.append(''.join(output))
        return

    # recursive case.
    element = int(digit[index])
    value = mapping[element]
    i = 0 
    while i < len(value):
        output.append(value[i])
        solve(digit,index+1,output.copy(),mapping,ans)
        output.pop()
        i += 1


if __name__ == '__main__':
    digit = "2345"
    ans = []
    output = []
    mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    index = 0
    solve(digit,index,output,mapping,ans)
    print(len(ans))


def solve(arr, index, ans, output):
    if index >= len(arr):
        if output not in ans:
            ans.append(output)
            return
    else:
        # exclude wali call .
        solve(arr, index+1, ans, output.copy())

        # include wali call .
        element = arr[index]
        output.append(element)
        solve(arr,index+1,ans,output.copy())


if __name__ == '__main__':
    arr = [1,2,2]
    index = 0 
    ans = [] 
    output = []    
    solve(arr, index, ans, output)
    print(ans)
# subsets

# [1,2,3] => [ [],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3] ]

# 2^3 = 8  == > 2^n.


def subsets(nums,index,output,ans):
    if index >= len(nums):
        ans.append(output)
        # print(ans)
        # input()
        return
    
    # exclude wali call.
    subsets(nums,index+1,output.copy(),ans)

    # include wali call.
    element = nums[index]
    output.append(element)
    subsets(nums,index+1,output.copy(),ans)
    


if __name__ == '__main__':
    nums = [1,2,3]
    index = 0
    output = []
    ans = []
    subsets(nums,index,output,ans)

    print(ans)


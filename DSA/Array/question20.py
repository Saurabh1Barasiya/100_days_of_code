from re import A


def addtion_of_two_arry(arr1,n,arr2,m):
    i = n-1
    j = m-1
    sum_ = 0
    carry = 0
    ans = []
    while i >= 0 and j >= 0 and m:
        val1 = arr1[i]
        val2 = arr2[j]
        sum_ = val1 + val2 + carry
        carry = sum_ // 10
        sum_ = sum_ % 10
        ans.append(sum_)
        i-=1
        j-=1

    # handle right array.
    while i >= 0:
        sum_ = arr1[i]+carry
        arr1.append(sum_)
        i-=1
    
    # handle left array.
    while j >= 0:
        sum_ = arr2[j]+carry
        arr2.append(sum_)
        j-=1
    
    # handle carry.
    while carry != 0 :
        sum_ = carry
        carry = sum_ // 10
        sum_ = sum_ % 10
        ans.append(sum_)
    ans.reverse()
    return ans

nums1 = [9,9,9]
nums1 = [9,9,9]
ans = addtion_of_two_arry(nums1,3,nums1,3)
print(ans)
# check array is sorted and rotated .

# [1,2,3,4,5] === > True 
# [1,1,1]     === > True 
# [3,4,5,1,2] === > True
# [3,5,7,1,6] === > False

def is_sorted_or_rotated(nums):
    i = 1
    count = 0
    n = len(nums)

    while i < n:
        if nums[i-1] > nums[i]:
            count += 1
        i += 1
    # check last and start value.
    if nums[n-1] > nums[0]:
        count += 1
    return count <= 1

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    # arr = [1,1,1]
    # arr = [3,4,5,1,2]
    # arr = [3,5,7,1,6] 
    ans = is_sorted_or_rotated(arr)
    print(ans)
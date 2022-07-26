# Amazone original queestion.

def solve(arr):
    if len(arr) == 2:
        return ''.join(list(map(str,arr)))
    else:
        final_array = []
        index = 0
        while index < len(arr)-1:
            add = arr[index] + arr[index+1]
            res = add % 10
            final_array.append(res)
            index += 1

        # recursive call.
        return solve(final_array)


if __name__ == '__main__':
    nums = [4,5,6,7]
    nums = [1,2,3,4]
    ans = solve(nums)
    print(ans)
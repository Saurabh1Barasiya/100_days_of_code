# Given an array of integers and a number k, find the maximum sum of a subarray of size k. 



# def slide(arr,k):
#     n=len(arr)
#     ans = []
#     i = 0
#     j = i+k-1
#     while j<n:
#         if i == 0:
#             current_max = sum(arr[i:j+1])
#             ans.append(current_max) 
#         else:
#             prvious_value = arr[i-1]            
#             next_value = arr[j]
#             s_sum = ans[i-1] - prvious_value + next_value
#             ans.append(s_sum)
#         i+=1
#         j += 1
#     print("Maximum sum is",max(ans))


def slide(arr,k):
    n = len(arr)
    if n < k:
        print("Can not find answer invalid inputs")
        return
    
    res = 0
    # find first k elements sum.
    for i in range(k):
        res += arr[i]
    

    # for remaning apply sliding window.
    i = 1
    while k < n:
        previous_value = arr[i-1]
        current_value = arr[k]
        current_sum = res - previous_value + current_value
        res = max(res,current_sum)
        i+=1
        k+=1
    print(res)



if __name__ == "__main__":
    arr = [100, 200, 300, 400]
    k = 2
    # arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    # k = 4
    slide(arr,k)
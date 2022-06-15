# def find_single_apprince(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i

def find_single_apprince(arr):
    ans = 0
    for i in arr:
        ans = ans ^ i 
    return ans

arr = [3,7,2,2,7,4,4,1,1]
ret_val = find_single_apprince(arr)
if ret_val is not None:
    print(ret_val)
else:
    print("Single value not found")

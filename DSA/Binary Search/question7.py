# import math
# n = int(input("Enter number to calculate square_root"))
# print("square_root of",n,"is",math.sqrt(n))




# n = int(input("Enter number to calculate square_root"))
# ans = -1
# for i in range(1,n+1):
#     if i*i == n:
#         print("square_root of",n,"is",i)
#         break
#     elif n > i*i :
#         ans = i
# else:
#     print("square_root of",n,"is",ans)


# print(len(list(range(0,37))))

# 👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀
# using binary search
def find_square_root(arr,s,e,key):
    start = s
    end = e
    mid = start+(end-start)//2
    ans = -1
    while start <= end:
        square = mid*mid
        if square == key:
            return mid
        if square < key:
            ans = mid 
            start = mid + 1
        else:
            end = mid - 1
        mid = start+(end-start)//2
    return ans

n = int(input("Enter number to calculate square_root"))
arr = list(range(0,n+1))
square = find_square_root(arr,0,len(arr)-1,n)
print("square_root of",n,"is",square)
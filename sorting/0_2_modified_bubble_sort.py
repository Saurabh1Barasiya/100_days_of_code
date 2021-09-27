arr = [34,15,29,8]
arr = [1,2,3,4,5,6]
round = 1
while round <= len(arr)-1:
    i = 0
    flag = 0
    print("round",round)
    while i <= len(arr)-1-round:
        if arr[i] > arr[i+1]:
            flag = 1
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        i+=1
    if flag == 0:
        print("round value",round)
        break
    round += 1
print(arr)


# Time complexcity worst case O(n^2).
# Time complexcity best case O(n).
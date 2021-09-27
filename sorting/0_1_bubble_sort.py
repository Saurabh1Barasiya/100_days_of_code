arr = [34,15,29,8]
round = 1
while round <= len(arr)-1:
    i = 0
    while i <= len(arr)-1-round:
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        i+=1
    round += 1
print(arr)


# Time complexcity worst case O(n^2).
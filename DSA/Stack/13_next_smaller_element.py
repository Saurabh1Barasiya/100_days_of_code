# next find smaller element in the array.

#     [4,8,5,2,25]
#     [2,5,2,-1,-1]

#     [13,7,6,12]
#     [7,6,-1,-1]

#     [13,13,21,3]
#     [3,3,3,-1]



def next_smaller_element(array):
    arr = []
    i = 0   
    while i < len(array):
        j = i+1
        if j == len(array):
            arr.append(-1)
        while j < len(array):
            if array[j] < array[i]:
                arr.append(array[j])
                break
            j+=1
        if len(array) == len(arr):
            return arr
        if j == len(array):
            arr.append(-1)
        i+=1
    return arr

if __name__ == '__main__':
    # array = [4,8,5,2,25]
    # array = [13,7,6,12]
    array = [13,13,21,3]
    ans = next_smaller_element(array)
    print(ans)

# Time complexcity worst case O(n^2)
# Space complexcity worst case O(n)
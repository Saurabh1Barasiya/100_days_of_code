# Rotate array by k elements.
def rotate(arr,k):
    temp = [0 for i in arr]
    i = 0
    while i < len(arr):
        temp[(i+k)%len(arr)] = arr[i]
        i += 1
    #arr = temp
    #return arr 

    # copy temp to arr
    for index,value in enumerate(temp):
        arr[index] = value
    return arr

if __name__ == '__main__':
    arr = [1,7,9,11]
    k = 2
    ans = rotate(arr,k)
    print(ans)
# First negative integer in every window of size k.

def slide(arr,k):
    n = len(arr)
    if n < k:
        print("Can not find answer invalid inputs")
        return
    
    
    # find first k elements sum.
    for i in range(k):
        if arr[i] < 0:
            print(arr[i],end=" ")
            break
    else:
        print(0,end=" ")
    

    # for remaning apply sliding window.
    i = 1
    j = k
    while j < n:
        m = i
        flag = False
        while m <= j:
            if arr[m] < 0:
                print(arr[m],end=" ")
                m = j+1
                flag = True
            m += 1
        if flag == False:
            print(0,end=" ")
        i+=1
        j+=1
    



if __name__ == "__main__":
    arr = [-8, 2, 3, -6, 10]
    k = 2
    # arr = [12, -1, -7, 8, -15, 30, 16, 28]
    # k = 3
    slide(arr,k)
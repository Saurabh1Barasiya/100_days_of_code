array = [12,45,23,51,19,8]

i = 0
while i < len(array)-1:
    print("pass",i)
    j = i + 1
    while j < len(array):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        j += 1
    i += 1
print(array)    
arr = [9,12,23,8,5]
arr = [36,47,90,49,98]
new_arr = []
arr.sort()
even_arrays=list(filter(lambda x: x%2==0, arr))
odd_arrays=list(filter(lambda x: x%2!=0, arr))

for i in range(len(even_arrays)): 
    new_arr.append(even_arrays[i])
    if i<len(odd_arrays):
        new_arr.append(odd_arrays[i])
print(new_arr)
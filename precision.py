'''

# Sample Input
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]


# Sample Output 

0.500000
0.333333
0.166667

'''


positive = 0
negative = 0
zero = 0
arr = [-4, 3, -9, 0, 4, 1]
for i in  arr:
    if i == 0:
        zero += 1
    elif i > 0:
        positive += 1
    elif i < 0:
        negative += 1
p = positive/len(arr)
n = negative/len(arr)
z = zero/len(arr)

print('%.6f'%p)
print('%.6f'%n)
print('%.6f'%z)

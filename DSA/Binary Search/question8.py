# Book allocation problem with O(n^2).

'''
arr  = [10,20,30,40]
i = 0
l1 = []
while i < len(arr)-1:
    # print(f"{i} pass {arr[0:i+1]}")
    # print(f"{i} pass {arr[i+1:]}")
    m1 = sum(arr[0:i+1])
    m2 = sum(arr[i+1:])
    # greater = m1 if m1 > m2 else m2
    # print("greater element ",greater)
    l1.append( m1 if m1 > m2 else m2)
    # l1.append(max([m1,m2]))
    # if m1>m2:
    #     l1.append(m1)
    # else:
    #     l1.append(m2)
    i += 1
print(l1)

#   [10,20,30,40]
#   [10] [20,30,40] ---> [10],[90] --> 90
#   [10,20],[30,40] ---> [30],[70] --> 70
#   [10,20,30],[40] ---> [60],[40] --> 60
#  [90,70,60] --> 60

'''
# ---------------------------------------------------------------------.
'''
arr  = [10,20,30,40]
i = 0
l1 = []
while i < len(arr)-1:
    m1 = sum(arr[0:i+1])
    m2 = sum(arr[i+1:])
    l1.append( m1 if m1 > m2 else m2)
    i += 1
print(min(l1))
'''
# ---------------------------------------------------------------------------------
# Book allocation problem with lesser code.

arr  = [10,20,30,40]
i = 0
l1 = []
while i < len(arr)-1:
    l1.append( sum(arr[0:i+1]) if sum(arr[0:i+1]) > sum(arr[i+1:]) else sum(arr[i+1:]))
    i += 1
print(l1)
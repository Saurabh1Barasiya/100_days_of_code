# class A:
#     def add(self,a,b):
#         return a+b
# class B(A):    
#    def add(self,a,b):
#         return a*b
# obj = B()
# print(obj.add(5,5))

# old_pass = []




# intput1 = input("")
# pw = input("")
# if intput1 == '123523':
#     print(15)
# elif intput1 == '10129':
#     print(10)


# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8]
# l3 = []
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print("Common element",l3)







n=int(input(""))
l = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
l.sort()
length = len(l)
mid = length//2
if length%2==0:
    midnext = mid -1
    print(l[mid]+l[midnext])
else:
    print(l[mid])



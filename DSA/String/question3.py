# reverse a string.

# first way.
name = 'saurabh'
print("Reverse of this string is ",name[::-1])

print("-------------------------------------------")
# second way.
name = 'saurabh'
rev = list(name)
rev.reverse()
print(''.join(rev))
print("-------------------------------------------")

# third way.
name = 'saurabh'
i = len(name)-1
while i >= 0 :
    print(name[i],end='')
    i -= 1
print()
print("-------------------------------------------")

# fourth way.
# 👀👀👀👀👀👀👀👀👀👀
# two pointers approach.

# loigc to sahi h but string is immutable in python.
# name = 'saurabh'
# start = 0
# end = len(name)-1
# while start <= end :
#     name[start],name[end] = name[end],name[start]
#     start += 1
#     end -= 1
# print(name)
name = ['s','a','u','r','a','b','h']
start = 0
end = len(name)-1
while start <= end :
    name[start],name[end] = name[end],name[start]
    start += 1
    end -= 1
print("".join(name))
print("-------------------------------------------")

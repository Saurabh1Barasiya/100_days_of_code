# Check if a string is palindrome or not.

# first way.
s = "noon"
print(s == s[::-1])


print("-------------------------------------------")
# secound way.
s = "noon"
rev = list(s)
rev.reverse()   
print(''.join(rev)==s)

print("-------------------------------------------")
# third way.
# two way pointer approach.
# 👀👀👀👀👀👀👀👀👀👀

s = "naman"
start = 0
end = len(s)-1
while start <= end :
    # print(s[start],s[end])
    if s[start] != s[end] :
        print("Not a palindrome")
        break
    start += 1
    end -= 1
else:
    print("String is Palindrom")
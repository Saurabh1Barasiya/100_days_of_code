# google question.

string = "aabbbaa"
start = 0
end = len(string)-1
l3 = []
while start < end:
    if string[start] == string[end]:
        l3.append(string[start]+string[end])
        start += 1
        end -= 1
        check = True
    else:
        check = False
        break
if check:
    l3.append(string[start]+string[end])
    while start > 0 and end <= len(string)-1:
        start-=1
        end+=1
        l3.append(string[start:end+1])

    l2 = l3[1:3]
    l2.reverse()
    del l3[1]
    del l3[2]
    for st in l3+l2:
        print(st, end=" ")
else:
    # print("string not palindrom")
    pass 
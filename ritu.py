# s = "abcdefabc"
# fin = "abc"
# s = list(s)
# s.insert(0,'0')
# s = ''.join(s)
# l = []
# for index,value in enumerate(s): 
#     c = s.find(fin,index)
#     if c == -1:
#         pass
#     else:
#         l.append(c)
# l2 = []
# for i in l:
#     if i not in l2:
#         l2.append(i)
# l3 = []
# for i in l2:
#     l3.append(str(i))
# print(''.join(l3))



def return_value(s,sub):
    s = list(s)
    s.insert(0,'0')
    s = ''.join(s)
    l = []
    for index,value in enumerate(s): 
        c = s.find(sub,index)
        if c == -1:
           pass
        else:
           l.append(c)
    l2 = []

    for i in l:
        if i not in l2:
            l2.append(i)
    
    l3 = []
    for i in l2:
        l3.append(str(i))
    return ''.join(l3)


# first test case..
# s = "abcdefabc"
# sub = "abc"



# secound test case.
s = "abcdabghabd"
sub = "ab#"
if '#' in sub:
    sub = list(sub)
    sub.remove('#')
    sub = ''.join(sub)

print(return_value(s,sub))





# l2 = []

# if l2:
#     print("list is not empty")
# else:
#     print("list is empty")



 

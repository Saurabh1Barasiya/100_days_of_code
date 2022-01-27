# s = "a"
# if s.isalnum():
#     print("yes")
# if s.isalpha():
#     print("yes")


numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n_check = False
l_check = False
u_check = False
s_check = False
s = list("ab1")
for i in numbers:
    if i in s:
       n_check = True
    if i in s:
       l_check = True
    if i in s:
       u_check = True
    if i in s:
       s_check = True
if n_check == False:
   s.append("A")
if l_check == False:
   s.append("a")
if n_check == False:
   s.append("1")
if s_check == False:
   s.append("@")

print("".join(s))
# original_string = "saasbh"
# original_string = "ssbh"
original_string = "saaaaaaauuuarbh"
original_string = "suuuarbh"
original_string = "sarbh"
original_string = "aaabbbdcccc"
original_string = "bbbdcccc"
original_string = "dcccc"

new_string = ""
i = 0 
flag = False   
while i < len(original_string)-1:
    if original_string[i] == original_string[i+1]:
        flag = True
        i+=1
        continue
    if flag:
        new_string += original_string[i+1::]
        break
                # flag = False
    else:
        new_string += original_string[i]
    i+=1
else:
    if original_string[i] != original_string[i-1]:
        new_string += original_string[i]
print(new_string)
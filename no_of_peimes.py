n = int(input("How many prime value you want to generate."))
breaking_value = n
count = 0
i = 0
while i < n:
    j = 2
    while j<i:
        if i%j == 0:
            break
        j = j + 1
    else:
        if i == 0 or i == 1:
            pass
        else:
            print("prime no ",i)
            n = n*10
            count = count+ 1
            if count == breaking_value:
                break
    i = i+1
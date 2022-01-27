def merge_the_tools(string, k):
    # your code goes here
    i = 0
    t = 0
    while i<len(string):
        if len(set(string[t:k]))>1:
            l1 = list(string[t:k])
            for j in string[t:k]:
                if l1.count(j)>1:
                    l1.pop(l1.index(j,1))   
            print(''.join(l1))
        else:
            print(string[t:k][0])
        k=k+3
        i=i+3
        t=t+3
        


s = "AAABCADDE"
# s = "AABCAAADA"
K = 3
merge_the_tools(s, K)

print(**{'x':'A'})
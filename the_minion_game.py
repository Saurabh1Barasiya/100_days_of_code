vovel = ['A','AN','ANA','ANAN','ANANA']
consonent = ['B','N','BA','NA','BAN','NAN','BANA','NANA','BANAN','BANANA']
consonent_count = []
vovel_count = []
for item in consonent:
    consonent_count.append(item.count(string))
for item in vovel:
        vovel_count.append(item.count(string))
    scc = sum(consonent_count)
    svc = sum(vovel_count)
    if scc>svc:
        print(f'Stuart {scc}')
    else:
        print(f'Kevin {svc}')
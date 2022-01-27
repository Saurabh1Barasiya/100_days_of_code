'''
Remove unbalanced parentheses in a given expression.

    Eg.) Input  : ((abc)((de))
         Output : ((abc)(de))  

         Input  : (((ab)
         Output : (ab) 
'''

q = list('((abc)((de))')
opening = q.count('(')
closing = q.count(')')
print(opening,closing)
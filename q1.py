# SyntaxWarning: invalid escape sequence \ 
# so we add a space in last occrence
s = "/dlrow/hello\eht\ "
s = s.replace("\\","/")
lo,l1,l2 = s.split('/')[1:4]
lo = lo[::-1]
l2 = l2[::-1]
print(''.join([l2,l1,lo]))
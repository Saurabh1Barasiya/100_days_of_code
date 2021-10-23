# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l = []
l1 = []

n = input()
for i in str(n):
    i = int(i)
    l.append(i)
s_u_m = sum(l)

if s_u_m > 26:
    new = str(s_u_m)
    for i in new:
      i = int(i)
      l1.append(i)
      n1 = sum(l1)
      n1 = n1-1
    print(al[n1])
else:
    print(al[s_u_m-1])
    

# check wether a no. prime or not.

n = 11

for  i in range(2,n):
    if  n%i == 0:
        print("Prime no.")
        break
else:
    if n == 2:
      print("prime no.")
    else:
        print("Not prime.")
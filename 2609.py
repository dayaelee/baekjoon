from math import gcd

a=input().split()
a[0]=int(a[0])
a[1]=int(a[1])
print(gcd(a[0], a[1]))
print((a[1]//gcd(a[0], a[1]))*(a[0]//gcd(a[0], a[1]))*gcd(a[0], a[1]))
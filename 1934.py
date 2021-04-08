import math
n=int(input())

a=list(input() for _ in range(n))

def lcm(a, b):
  return a*b//math.gcd(a, b)

for i in range(n):
  b=a[i].split( )
  b[0]=int(b[0])
  b[1]=int(b[1])
  print(lcm(b[0], b[1]))
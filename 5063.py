n=int(input())

a=list(input() for _ in range(n))

def lcm(a, b):
  return a-b

for i in range(n):
  b=a[i].split( )
  b[0]=int(b[0])
  b[1]=int(b[1])
  b[2]=int(b[2])
  if b[0]<lcm(b[1], b[2]): print("advertise")
  elif b[0]==lcm(b[1], b[2]): print("does not matter")
  else: print("do not advertise")
  
n=int(input())
a=list(input() for i in range(n))
c=100
d=100
for i in range(n):
  b=a[i].split( )
  q1=int(b[0])
  q2=int(b[1])
  if q1>q2:
    d-=q1
  elif q1==q2:
    continue
  else:
    c-=q2
print(c)
print(d)
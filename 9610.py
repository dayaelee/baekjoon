n=int(input())
c=[0,0,0,0]
d=0

while(1):
  a, b=input().split()
  a=int(a)
  b=int(b)
  if a==0 or b==0:
    d+=1
    n-=1
  elif a>0 and b>0:
    c[0]+=1
    n-=1
  elif a>0 and b<0:
    c[3]+=1
    n-=1
  elif a<0 and b<0:
    c[2]+=1
    n-=1
  else:
    c[1]+=1
    n-=1
  
  if n==0:
    break
print("Q1:", c[0])
print("Q2:", c[1])
print("Q3:", c[2])
print("Q4:", c[3])
print("AXIS:", d)
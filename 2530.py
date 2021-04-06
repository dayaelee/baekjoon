a, b, c = input().split( )
d = int(input())
a=int(a)
b=int(b)
c=int(c)
if d+c>59:
  if d+c==60:
    b+=1
    c=0
  elif d+c>59:
    b+=(d+c)/60
    c=(d+c)%60
  if b==60:
    a+=1
    b=0
  elif b>59:
    a+=b/60
    b=b%60
else:
  c+=d
  if c==60:
      b+=1
      c=0
  elif c>59:
      b+=c/60
      c=c%60
if a==24:
  a=0
elif a>24:
  a=a%24
print(int(a), int(b), c)
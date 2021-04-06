a, b = input().split( )
c = int(input())

a=int(a)
b=int(b)


if b+c>59:
  a+=(b+c)/60
  if a==24:
    a=0
  elif a>24:
    a=a-24
    
  b=(b+c)%60
else:
  b += c

print(int(a), b)
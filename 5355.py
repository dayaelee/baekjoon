n=int(input())
a=list(input() for i in range(n))
for i in range(n):
  b=a[i].split( )
  c=float(b[0])
  for j in range(len(b)):
    if b[j]=='@':
      c*=3
    elif b[j]=='%':
      c+=5
    elif b[j]=='#':
      c-=7
  print('%.2f' %c)
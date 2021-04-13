a=0
b=1
n=int(input())
if n==1:
  print('1')
elif n==0:
  print('0')
  
while(n-1):
  c=a+b
  a,b= b,c
  if n==2:
    print(c, end=" ")
  n=n-1
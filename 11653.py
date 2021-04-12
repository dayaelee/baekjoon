n=int(input())
while(1):
  for i in range(10000000):
    if i==0 or i==1:
      continue
    if n%i==0:
      print(i)
      n=n//i
      break
  if(n==1):
    break
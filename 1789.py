n=int(input())
while(1):
  for i in range(4294967295):
    if i==0:
      continue
    n=n-i
    if n<0:
      break
  print(i-1)
  break
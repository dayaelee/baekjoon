while(1):
  a=int(input())
  if(a==-1):
    break

  sum=0
  p= str(a)+' = '

  for i in range(a):
    if i==0:
      continue
    elif a%i==0:
      if i!=1:
        p+=' + '
      sum+=i
      p+= str(i)
    
  if sum==a:
    print(p)
  else:
    print(str(a)+' is NOT perfect.')
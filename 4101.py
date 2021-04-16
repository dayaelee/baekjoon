while(1):
  
  n=input().split()
  n[0]=int(n[0])
  n[1]=int(n[1])
  if(n[0]==0 and n[1]==0):
    break
  
  if(n[0]>n[1]):
    print('Yes')
  else:
    print('No')
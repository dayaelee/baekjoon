num=int(input())
mmax=0

for i in range(num):
  n=input().split()
  temp=0
  max=0
  result=0
  for i in range(3):
    n[i]=int(n[i])

  if n[0]==n[1]==n[2]:
    result=(n[0]*1000)+10000
  else:
    if n[0]==n[1]:
      result=(n[0]*100)+1000
    elif n[1]==n[2]:
      result=(n[1]*100)+1000
    elif n[0]==n[2]:
      result=(n[0]*100)+1000
    else:
      for i in range(3):
        if max<n[i]:
          max=n[i]
      result=max*100 

  if i==0:
    mmax=result
  elif i!=0 and mmax<result:
    mmax=result
print(mmax)

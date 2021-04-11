n = int(input())
count=0
notcount=0
for i in range(n):
  a=int(input())
  if a==1:
    count+=1
  else:
    notcount+=1
    
if count<notcount:
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')

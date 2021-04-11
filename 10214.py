n = int(input())
if n==0:
  quit()

ycount=0
kcount=0

for i in range(n):
  for i in range(9):
    a=input().split()
    if a[0]>a[1]:
      ycount+=1
    elif a[0]<a[1]:
      kcount+=1
      print(kcount)
    else:
      continue

 
  if ycount>kcount:
    print('Yonsei')
  elif ycount<kcount:
    print('Korea')
  else:
    print('Draw')

  ycount=0
  kcount=0
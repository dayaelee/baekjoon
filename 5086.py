while(1):
  a=input().split()
  a[0]=int(a[0])
  a[1]=int(a[1])

  if a[0]==0 and a[1]==0:
    break

  if a[1]%a[0]==0:
    print('factor')
  elif a[0]%a[1]==0:
    print('multiple')
  else:
    print('neither')
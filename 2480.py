n=input().split()
temp=0
max=0
for i in range(3):
  n[i]=int(n[i])

if n[0]==n[1]==n[2]:
  print((n[0]*1000)+10000)
else:
  if n[0]==n[1]:
    print((n[0]*100)+1000)
  elif n[1]==n[2]:
    print((n[1]*100)+1000)
  elif n[0]==n[2]:
    print((n[0]*100)+1000)
  else:
    for i in range(3):
      if max<n[i]:
        max=n[i]
    print(max*100)
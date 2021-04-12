t=input()
len(t)
c=0
if len(t)%2==0:
  for i in range(len(t)//2):
    if t[i]==t[-i-1]:
      c=1
      continue
    else:
      c=0
      break
elif len(t)%2==1:
  for i in range(len(t)//2):
    if i==(len(t)//2):
      break
    else:
      if t[i]==t[-i-1]:
        c=1
        continue
      else:
        c=0
        break
if len(t)==1:
  c=1
print(c)
    
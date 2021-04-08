b=input()
n=len(b)
height=10

for i in range(n+1):
  if i==0:
    continue
  if b[i-1:i]==b[i:i+1]:
    height+=5
    if i+1==n:
      break
  else:
    height+=10
    if i+1==n:
      break
print(height)
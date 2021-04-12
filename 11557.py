t=int(input())
max=0
for j in range(t):
  n=int(input())
  for i in range(n):
    a=input().split()
    if max<int(a[1]):
      max=int(a[1])
      who=a[0]
  print(who)
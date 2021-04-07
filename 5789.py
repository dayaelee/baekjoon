n=int(input())
a=list(input() for i in range(n))

for i in range(n):
  b=len(a[i])//2
  if a[i][b-1]==a[i][b]:
    print("Do-it")
  else:
    print("Do-it-Not")

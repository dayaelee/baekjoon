n = int(input())
cnt=0
for i in range(n-1):
    cnt+=((n-(i+1))*((n+1)-(n-i+1)))
print(cnt)
print(3)
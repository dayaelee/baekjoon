n=int(input())
a=list(map(int, input().split()))

dp=[1]*n
dp2=[1]*n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

a=a[::-1]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp2[i]=max(dp2[i], dp2[j]+1)
dp2=dp2[::-1]
#print('dp2', dp2[::-1])
result=0
for i in range(n):
    result=max(dp[i]+dp2[i], result)

print(result-1)
# 10
# 1 5 2 1 4 3 4 5 2 3 1

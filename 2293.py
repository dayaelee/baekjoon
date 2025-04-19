import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nlist=[]
for i in range(n):
    nlist.append(int(input()))

dp=[0]*(k+1)

dp[0]=1

for i in range(n):
    v=nlist[i]
    for j in range(v, k+1):
        dp[j] = dp[j]+ dp[j-v]
# print(dp)
print(dp[-1])
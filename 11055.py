n = int(input())
A =[0] + list(map(int, input().split()))

dp=[0] + [A[i] for i in range(1, n+1)]

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if A[j]>A[i]:
            dp[j]=max(dp[j], A[j]+dp[i])
print(max(dp))
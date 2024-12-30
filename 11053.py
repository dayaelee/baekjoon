n = int(input())
A = list(map(int, input().split()))

dp=[ ]
for i in range(len(A)):
    maxValue = 0
    for j in range(len(dp)):
        
        if A[j] < A[i]:
            if maxValue < dp[j]:
                maxValue=dp[j]
    dp.append(maxValue+1)
print(max(dp))



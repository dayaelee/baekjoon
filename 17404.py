import sys 
input = sys.stdin.readline

n = int(input())
ccosts=[]
for i in range(n):
    ccosts.append(list(map(int, input().split())))

dp= [[0] * 3 for _ in range(2)]

ans = float("inf")
for k in range(3):
    dp[0][0], dp[0][1], dp[0][2] = float("inf"), float("inf"), float("inf")
    dp[0][k]= ccosts[0][k]

    for i in range(1, n):
        dp[1][0] = min(dp[0][1], dp[0][2]) + ccosts[i][0]
        dp[1][1] = min(dp[0][0], dp[0][2]) + ccosts[i][1]
        dp[1][2] = min(dp[0][0], dp[0][1]) + ccosts[i][2]


        dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
    ans = min(ans, min(dp[0][(k+1)%3], dp[0][(k+2)%3]))
print(ans)
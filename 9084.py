import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    basket = [[0,0]] + list(map(int, input().split()))
    m = int(input()) # target

    # 이차원 배열로 

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for ii in range(n+1):
        dp[ii][0]= 1
    
    for ii in range(1, n+1):
        for jj in range(1, m+1):
            dp[ii][jj] = dp[ii-1][jj]
            if jj-basket[ii] >= 0:
                dp[ii][jj] += dp[ii][jj-basket[ii]]

    print(dp[n][m])




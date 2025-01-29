import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ntotal=[]

for i in range(n):
    ntotal.append(list(map(int, input().split())))

dp=[[0 for _ in range(n+1)],[0, ntotal[0][0]]]
for i in range(1, n+1):
    if i == 1:
        for j in range(2, n+1):
            dp[i].append(dp[i][j-1]+ntotal[i-1][j-1])
    else:
        dp.append([0])
        dp[i].append(dp[i-1][1]+ntotal[i-1][0])
        for j in range(2, n+1):
            dp[i].append(dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+ntotal[i-1][j-1])

for i in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    result=0
    if x1 == y1 == 1 and x2 == y2 == n:
        print(dp[n][n])
    elif x1==x2 and y1==y2:
        print(ntotal[y2-1][x2-1])
    else:
        result = dp[y2][x2]-dp[y2][x1-1]-dp[y1-1][x2]+dp[y1-1][x1-1]
        print(result)

import sys
input = sys.stdin.readline
mapp=[]
n = int(input())
for i in range(n):
    mapp.append(list(map(int, input().split())))
dp= [[float("inf")] * n for _ in range(n)]

graph=[[]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mapp[i][j]==1:
            graph[i].append(j)
            graph[j].append(i)
            dp[i][j]= 1
#             dp[j][i]= 1
# print(graph)

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j]=0
# print(dp)

for k in range(n):
    for a in range(n):
        for b in range(n):
            if dp[a][k]==1 and dp[k][b]==1:
                dp[a][b] = 1


for a in range(n):
    for b in range(n):
        if dp[a][b]!=1:
            dp[a][b]=0


# print(dp)
for i in dp:
    print(' '.join(map(str, i)))

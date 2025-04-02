import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin = sorted(list(set(coin)))

dpp=[float("inf")]*(k+1)
dpp[0]=0

for c in coin:
    for j in range(1, k+1):
        if j-c>=0:
            dpp[j]=min(dpp[j-c]+1, dpp[j])
ans = dpp[k]
if ans == float("inf"):
    print(-1)
else:
    print(ans)
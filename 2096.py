import sys
input = sys.stdin.readline

n=int(input())

mapp=list(map(int, input().split()))

dp=mapp
dp2=mapp

for i in range(1, n):
    a, b, c = map(int, input().split())
    dp=[
        max(dp[0], dp[1])+a,
        max(dp)+b,
        max(dp[1], dp[2])+c,
    ]

    dp2=[
        min(dp[0], dp[1])+a,
        min(dp)+b,
        min(dp[1], dp[2])+c,
    ]
print(max(dp), min(dp2))

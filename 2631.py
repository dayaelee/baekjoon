import sys
input = sys.stdin.readline

n = int(input())
kids=[]
for i in range(n):
    kids.append(int(input()))
dp = [1 for _ in range(n+1)]
for i in range(0, n):
    tmp = []
    for k in range(0, i):
        if kids[i]>kids[k]:
            dp[kids[i]]=max(dp[kids[k]]+1, dp[kids[i]])
print(n-max(dp))
    


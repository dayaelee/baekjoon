import sys

input = sys.stdin.readline

t = int(input())

dp=[1, 2, 4]

start = 0
end = start+2

for i in range(7):
    sum = 0
    for j in range(start, end+1):
        sum+=dp[j]
    start+=1
    end+=1
    dp.append(sum)

# print(dp)


for i in range(t):
    n = int(input())
    print(dp[n-1])

import sys
input = sys.stdin.readline

t= int(input())
dp=[1]*10001


for i in range(2, 10001):
    dp[i]+=dp[i-2]

# for i in range(10):
#     print('^^', dp[i])
for i in range(3, 10001):
    dp[i]+=dp[i-3]

# for i in range(10):
#     print('^^', dp[i])

for i in range(t):
    n=int(input())
    
    print(dp[n])



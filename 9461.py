import sys
input = sys.stdin.readline



t = int(input())
for i in range(t):
    dp=[0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    get = int(input())

    if get < 11:
        print(dp[get])
    else:
        for i in range(11, get+1):
            tmp = dp[i-3] + dp[i-2] 
            dp.append(tmp)
            print(dp)
        print(dp[get])



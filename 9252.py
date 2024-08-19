s1 = input()
s2 = input()

m=len(s1)
n=len(s2)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])

result =''
startm = m
startn = n

print(max(dp[-1]))
if max(dp[-1])!=0:
    while 1:
            if dp[startm][startn]==0:
                break
            # 위에것이 더 큰지
            if dp[startm][startn] == dp[startm-1][startn]:
                startm-=1
            elif dp[startm][startn] == dp[startm][startn-1]:
                startn-=1
            elif ((dp[startm][startn]-1) == dp[startm-1][startn-1]):
                
                startm-=1
                startn-=1

                result+=s2[startn]

            # 왼쪽 것이 더 큰지

            # 둘다 안크면 대각선 이동 
            # 값도 넣어줌 

    print(result[::-1])
n = int(input())
p = [0]+list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(1, n+1): # p1~pN까지 처리
    for j in range(1, n+1): #카드 1장~N장까지 추가
        if j-i>=0: #dp[] 범위내
            dp[j]= max(dp[j], dp[j-i]+p[i])
print(dp[n])
    
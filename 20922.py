n, k = map(int, input().split())
nL = list(map(int, input().split()))

start = 0
end = 1

if n == 1:
    print(1)
    exit()

global checkCnt
checkCnt =0

dp= [0] * 100001
dp[nL[start]] = 1
dp[nL[end]] += 1
cnt = 2
while end<n:
    if dp[nL[end]]>k:
        if end == n-1:
            cnt-=1
            checkCnt = max(cnt, checkCnt)
        dp[nL[start]]-=1
        if dp[nL[end]]>k:
            start +=1
            if start>end:
                break
            cnt-=1
            checkCnt = max(cnt, checkCnt)
        else:
            start+=1
            end+=1
            if end >=n:
                break
            dp[nL[end]]+=1
    else:
        end+=1
        if end>=n:
            break
        cnt +=1
        dp[nL[end]]+=1
checkCnt = max(cnt, checkCnt)

print(checkCnt)
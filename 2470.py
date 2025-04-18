n = int(input())
nList = sorted(list(map(int, input().split())))

start=0
end=len(nList)-1

result=float("inf")
dp=[0, 0]

while start < end:

    if result > abs(nList[start]+nList[end]):
        result = abs(nList[start]+nList[end])
        dp[0], dp[1] = nList[start], nList[end]
        if result==0:
            break
    print((nList[start]+nList[end]), start, end)
    if nList[start]+nList[end]<0:
        start+=1
    elif nList[start]+nList[end]>0:
        end-=1
print(' '.join(map(str, dp)))
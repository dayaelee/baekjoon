import heapq
n, k = map(int, input().split())
visited = [False] * 100002
dp=[float("inf")] * 100002
def dijckstra(start, target):
    hq = [(0, start)]
    dp[start] = 0
    while hq:
        #print(hq)
        nowtime, now = heapq.heappop(hq)
        visited[now] = True
        if now == target:
            print(nowtime)
            break
            
        if 0<=now+1<=100000 and visited[now+1]==False:
            if dp[now+1]>dp[now]+1:
                dp[now+1]=dp[now]+1
                heapq.heappush(hq, (nowtime+1, now+1))
        
        if 0<=now-1<=100000 and visited[now-1]==False:
            if dp[now-1]>dp[now]+1:
                dp[now-1]=dp[now]+1
                heapq.heappush(hq, (nowtime+1, now-1))

        if 0<=now*2<=100000 and visited[now*2]==False:
            if dp[now*2]>dp[now]:
                dp[now*2]=dp[now]
                heapq.heappush(hq, (nowtime, now*2))
dijckstra(n, k)
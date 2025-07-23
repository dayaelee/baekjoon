import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def topology_sort(): # 위상정렬
    q = deque([])

    for i in range(1, n+1): # 어디서 부터 들어갈지 항상 바뀜 = 진입차수가 0인것을 넣기 
        if indegree[i]==0:
            q.append(i)
            dp[i] = delay[i] # 건물 짓기 

    while q:
        now = q.popleft()
        
        for i in graph[now]: # 관련 노드들 확인
            indegree[i] -=1 # 진입차수 끊어주기 
            dp[i] = max(dp[i], dp[now] + delay[i]) # 관련 노드의 건설시간, # 나의 건설된 시간 + 지금 짓는 건물 
            #관련 노드들의 건설 시간에 대해 젤 큰 값으로 갱신해줌 
            if indegree[i]==0: # 진입차수가 0인건 다시 넣어줌 
                q.append(i)
    print(dp[w])

for i in range(t):

    n, k = map(int, input().split())
    # 진입차수 
    indegree = [0] * (n+1)
    dp = [0 for _ in range(n+1)]
    delay=[0]+list(map(int, input().split()))
    graph= [[] for _ in range(n+1)]
    for j in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1 # 진입차수 설정
    w=int(input())

    topology_sort()
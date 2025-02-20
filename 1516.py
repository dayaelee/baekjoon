import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
building=[] # nlogn
for i in range(n):
    # 건물 짓는데 걸리는 시간, 선행 건물 번호 
    building.append(list(map(int, input().split())))
# 진입 차수
indegree = [0] * (n+1)

time = [0]
before = [[0]]
for i in building:
    tmp =[]
    for j in range(len(i)):
        if j == 0:
            time.append(i[0])
        elif 0<j<=len(i)-2:
            tmp.append(i[j])
            
    if len(i)==2:
        tmp.append(0)
        before.append(tmp)
    else:
        before.append(tmp)

graph= [[] for _ in range(n+1)]
for i in range(1, len(before)):
    for j in before[i]:
        if j == 0:
            continue
        graph[j].append(i)
        indegree[i]+=1

# dp 초기화 
dp=[0 for _ in range(n+1)]

# print('indegree, ', indegree)

def weesang():
    result = []
    q = deque()

    for i in range(1, n+1):
        # 진입 차수가 0인 정점이면?
        if indegree[i] ==0:
            q.append(i)
            dp[i]=time[i]
    #tmp=[]
    while q:
        curr = q.popleft()
        result.append(curr)
        # print('hi', curr)
        # print('dp', dp)
        for i in graph[curr]:
            # print('hi curr', curr, 'i', i, 'indegree[i]', indegree[i])
            #curr로부터 나가는 간선 제거
            #tmp.append(dp[curr])
            indegree[i] -=1
            dp[i] = max(dp[i], dp[curr]+time[i])

            if indegree[i]==0:
                # #dp[i]+=dp[curr]
                # print('tmp:', tmp)
                q.append(i)
                # print('curr', curr, 'i', i)
                # print('?????', dp[i], time[i], dp[curr])
                # if dp[i]<max(tmp)+time[i]:
                #     dp[i]=max(tmp)+time[i]
                #     tmp=[]
                
weesang()
for i in range(1, len(dp)):
    print(dp[i])


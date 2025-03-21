import sys
from collections import deque
sys.setrecursionlimit(100000)

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
# 년 카운팅
# for문으로 첨부터 끝까지 조회, dfs 두덩어리 이상인가?

#전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0

n, m = map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(visited, i, j, arr, q):
    cnt = 0
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if arr[ny][nx]==0:
            cnt+=1
        elif arr[ny][nx]>0:
            if visited[ny][nx]==False:
                visited[ny][nx]= True
                visited, arr, q = dfs(visited, ny, nx, arr, q)
    q.append((i, j, cnt))
    return visited, arr, q
                        

time = 0
while 1:
    visited=[[False]*m for _ in range(n)]
    q=deque([])
    cnt = 0

    realCheck = 0
    for i in arr:
        check = max(i)
        realCheck=max(realCheck, check)
    if realCheck ==0:
        print(0)
        exit()
    else:
        # print('?')
        for i in range(1, n):
            for j in range(1, m):
                if arr[i][j]>=1 and visited[i][j]==False:
                    cnt+=1
                    visited[i][j]=True
                    visited, arr, q  = dfs(visited, i, j, arr, q)
        for i in q:
            yy, xx, cntt=i
            arr[yy][xx]-=cntt
            if arr[yy][xx]<0:
                arr[yy][xx]=0
    time+=1

    # print()
    # print('cnt', cnt, 'time', time)
    # for i in arr:
    #     print(i)
    # print()

    # if time ==4:
    #     break
    if cnt >=2:
        print(time-1)
        break
    

    

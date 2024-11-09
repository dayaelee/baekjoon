from collections import deque

dy=[-1, 1, 0, 0]
dx=[0, 0, -1, 1]
global cnt

n = int(input())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, list(input()))))

visited= [[False for _ in range(n)] for _ in range(n)]
def dfs(startY, startX):
    cnt= 1
    queue=deque([(startY, startX)])
    visited[startY][startX]=True
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            yy = dy[i]+y
            xx = dx[i]+x

            if 0<=yy<n and 0<=xx<n and mapp[yy][xx]>=1 and visited[yy][xx] == False:
                
                cnt +=1

                visited[yy][xx]= True 

                mapp[yy][xx] = cnt
                queue.append((yy, xx))
        
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if mapp[i][j]==1:
            result.append(dfs(i, j))
result = sorted(result)

print(len(result))
for i in result:
    print(i)





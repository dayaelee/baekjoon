from collections import deque
dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

n, m = map(int, input().split())
mapp=[]

# print()

for i in range(n):
    mapp.append(list(map(int, list(input()))))
    # print(mapp[i])

visited=[[[False]*2 for _ in range(m)] for _ in range(len(mapp))]

cnt=0

q=deque([(0, 0, cnt, 1)])
global answer
answer=-1
def bfs():
    cnt=1

    q=deque([(0, 0, cnt, 1)])
    visited[0][0][1]=True
    global answer
    
    while q:
        # print('q', q)
        y, x, cnt, able = q.popleft()

        if y==n-1 and x== m-1:
            print(cnt)
            exit()
            
            return cnt

        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]

            if 0<=ny<n and 0<=nx<m:
                if mapp[ny][nx]==0:
                    if able>0:
                        if visited[ny][nx][1]==False:
                            visited[ny][nx][1]=True
                            q.append((ny, nx, cnt+1, able))
                    else:
                        if visited[ny][nx][0]==False:
                            visited[ny][nx][0]=True
                            q.append((ny, nx, cnt+1, able))
                else: # 1일 때 
                    if able>0:
                        if visited[ny][nx][1]==False:
                            visited[ny][nx][1]=True
                            q.append((ny, nx, cnt+1, able-1))

bfs()

print(-1)
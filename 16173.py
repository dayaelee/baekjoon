from collections import deque
dy=[0, 1]
dx=[1, 0]

n = int(input())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))
def bfs(y, x, lenn):
    queue= deque([(y, x, lenn)])
    while queue:
        y, x, length = queue.popleft()
        
        for i in range(2):
            ny = y + (dy[i] * length)
            nx = x + (dx[i] * length)
            if 0<=ny<n and 0<=nx<n:
                if ny==n-1 and nx==n-1:
                    return True
                else:
                    if mapp[ny][nx]>0:
                        Nlength = mapp[ny][nx]
                        queue.append((ny, nx, Nlength))
    return False
        
if bfs(0, 0, mapp[0][0])==False:
    print('Hing')
else:
    print("HaruHaru")
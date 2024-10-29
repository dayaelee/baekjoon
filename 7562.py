
from collections import deque
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input()) # 테스트케이스 개수
for i in range(t):
    l = int(input()) # 체스판의 한 변의 길이
    y, x = map(int, input().split()) # 현재 나이트가 있는 칸
    goalY, goalX = map(int, input().split()) # 나이트가 이동하려고 하는 칸
    visited= [[False] * l for _ in range(l)]

    def bfs(y, x, goalY, goalX):
        
        queue = deque([(y, x, 0)])
        while queue:
            ny, nx, cnt = queue.popleft()

            if ny==goalY and nx ==goalX:
                return cnt

            for i in range(8):
                nny = ny + dy[i]
                nnx = nx + dx[i]

                if 0<=nny<l and 0<=nnx<l and visited[nny][nnx]==False:
                    visited[nny][nnx]=True
                    queue.append((nny, nnx, cnt+1))

    print(bfs(y, x, goalY, goalX))
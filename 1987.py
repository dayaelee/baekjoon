import sys
from collections import deque
input = sys.stdin.readline

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

visited=[False for _ in range(26)] # 0번은 쓰지않음

r, c = map(int, input().split())
mapp=[list(map(lambda x: ord(x)-65, input().strip())) for i in range(r)]

result = 0
def backtrack(starty, startx, cnt):
    global result 
    result = max(cnt, result)

    for i in range(4):
        ny = starty + dy[i]
        nx = startx + dx[i]

        if 0<= ny <len(mapp) and 0 <= nx <len(mapp[0]):
            realTarget = mapp[ny][nx]
            if visited[realTarget] == False:
                visited[realTarget] = True
                backtrack(ny, nx, cnt+1)
                visited[realTarget] = False

backtrack(0, 0, 1)
print(result)

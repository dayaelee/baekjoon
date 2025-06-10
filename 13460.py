import sys
from collections import deque
import copy
input = sys.stdin.readline

dy=[1, -1, 0, 0] # 하, 상, 좌, 우
dx=[0, 0, -1, 1]

n, m = map(int, input().split())
b =[]
for i in range(n):
    b.append(list(input().strip()))
    print(b[i])

def move(ry, rx, dir, b, color):
    fell=0
    b[ry][rx]='.'
    while 1:
        ty, tx = ry + dy[dir], rx + dx[dir]
        if b[ty][tx]== '#':
            break
        if b[ty][tx]== 'O':
            fell = 1
            ry, rx = ty, tx
            break
        if b[ty][tx] == '.':
            ry, rx = ty, tx
            continue
        break

    # if not fell:
    #     b[ry][rx]=color

    return ry, rx, fell        

def bfs(balls, b):
    visited=[[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

    cnt = 0
    ry, rx =balls[0]
    by, bx =balls[1]

    visited[ry][rx][by][bx]=True

    q = deque([(ry, rx, by, bx, cnt, copy.deepcopy(b))]) # 0은 빨간공, 1은 파란공 
    
    while q:
        ry, rx, by, bx, cnt, b = q.popleft()
        
        for i in range(n):
            print(b[i])
        
        if cnt>=10:
            print(-1)
            sys.exit(0)   
            
        for ddir in range(4):
            nb = copy.deepcopy(b)

            first, second = 'R', 'B'
            if ddir ==0 and ry < by : first, second = 'B', 'R'
            if ddir ==1 and ry > by : first, second = 'B', 'R'
            if ddir ==2 and rx > bx : first, second = 'B', 'R'
            if ddir ==3 and rx < bx : first, second = 'B', 'R'


            if first == 'R':
                nry, nrx, redHole= move(ry, rx, ddir, nb, 'R')
                nby, nbx, blueHole= move(by, bx, ddir, nb, 'B')
            else:
                nby, nbx, blueHole= move(by, bx, ddir, nb, 'B')
                nry, nrx, redHole= move(ry, rx, ddir, nb, 'R')
                
            if blueHole:
                continue

            if redHole:
                print(cnt+1)
                return
            
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx]=True
                q.append([nry,nrx,nby,nbx, cnt+1, copy.deepcopy(nb)])

# 공 찾는 것 
def findBalls():
    balls=[[], []]
    for i in range(n):
        for j in range(m):
            if b[i][j]=='R':
                balls[0]=[i, j]
            elif b[i][j]=='B':
                balls[1]=[i, j]
    return balls

balls = findBalls() # 0번째 인덱스에 R, 1에 B 
bfs(balls, b)
# 가로, 세로, 대각선
import sys 
input = sys.stdin.readline

dy=[1, -1, 0, 0, 1, 1, -1, -1]
dx=[0, 0, -1, 1, -1, 1, -1, 1]

while 1:
    w, h = map(int, input().split())
    if w == 0 and h ==0:
        break
    mapp=[]
    for i in range(h):
        mapp.append(list(map(int, input().split())))
    visited=[[False for i in range(w)] for i in range(h)]
    #print(visited)
    
    startY=0
    startX=0
    def bfs(startY, startX):
        queue=[[startY, startX]]
        visited[startY][startX]=True
        while queue:
            y, x = queue.pop()
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<h and 0<=nx<w:
                    if visited[ny][nx]==False:
                        if mapp[ny][nx]==1:
                            visited[ny][nx]=True
                            queue.append([ny, nx])
    global total        
    total = 0
    for i in range(h):
        for j in range(w):
            if mapp[i][j]==1 and visited[i][j]==False:
                total+=1
                bfs(i, j)
    print(total)

    

    

import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

mapp=[]
for i in range(r):
    mapp.append(list(map(int, input().split())))

checkk=0
for i in range(r):
    for j in range(c):
        if mapp[i][j]==1:
            checkk+=1

zeros=[] # 빈칸 모음
for i in range(r):
    for j in range(c):
        if i ==0 or i== r-1 or j==0 or j==c-1:
            zeros.append([i, j])

# print('zeros', zeros)

visited = [[False] * c for _ in range(r)]

def bfs(zeros, cnt, check):
    # print('cnt, ', cnt, 'check', check)

    ends=[]
    for i in zeros:
        y, x = i
        if visited[y][x]==False:
            q=deque([(y, x)])
            while q:
                yy, xx = q.popleft()
                if mapp[yy][xx]==0 and visited[yy][xx]== False:
                    for i in range(4):
                        ny = yy+dy[i]
                        nx = xx+dx[i]

                        if 0<=ny <r and 0<=nx<c and visited[ny][nx]==False:
                            if mapp[ny][nx]==1:
                                ends.append((ny, nx))
                            elif mapp[ny][nx]==0:
                                visited[yy][xx]=True
                                q.append((ny,nx))
    if not ends:
        # print('check!', check)
        return [cnt, check]
    
    # print(ends, 'ends: ' ,len(ends))

    for i in ends:
        y, x = i
        mapp[y][x]=0
    
    # print()
    # for i in mapp:
    #     print(' '.join(map(str,i)))

    checkk = 0
    for i in range(r):
        for j in range(c):
            if mapp[i][j]==1:
                checkk+=1
                check.append(checkk)
    # print('check', check)
    return bfs(ends, cnt+1, check)

answer = bfs(zeros, 0, [])
# print('answer', answer)
print(answer[0])
if not answer[1]:
    print(checkk)
else:
    print(answer[1][-1])
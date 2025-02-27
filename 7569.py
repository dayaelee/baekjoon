import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# m 가로 n 세로 h 올려지는 수 
m, n, h = map(int, input().split())
bigMap=[]
mapp =[]
for j in range(h):
    mapp =[]
    for i in range(n):
        mapp.append(list(map(int, input().split())))
    bigMap.append(mapp)

# cnt = 0
# for k in range(h):
#     for j in range(n):
#         for q in range(m):
#             if bigMap[k][j][m]==0:
#                 cnt += 1
#                 break
# if cnt ==0:
#     print(0)
# else:
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
total = 0
q = deque([])
for k in range(h):
    for j in range(n):
        for i in range(m):
            if bigMap[k][j][i]==1:
                q.append((k, j, i))
                visited[k][j][i]=True
                # for x in range(6):
                #     if x < 4:
                #         ny = j + dy[x]
                #         nx = i + dx[x]
                #         nh = k
                #     elif x ==4:
                #         ny = j
                #         nx = i
                #         nh = k+1
                #     elif x ==5:
                #         ny = j
                #         nx = i
                #         nh = k-1

                #     if 0<=nh<h and 0<=ny<n and 0<=nx<m:
                #         if bigMap[nh][ny][nx]==0:
                #             # bigMap[nh][ny][nx]=2
                #             q.append((nh, ny, nx, 1))

while q:
        #print('q ', q)
        hh, y, x = q.popleft()
        # print('hh, y, x: ', hh, y, x)
        # bigMap[hh][y][x] = value+1
        for i in range(6):
            if i < 4:
                ny = y + dy[i]
                nx = x + dx[i]
                nh = hh
            elif i ==4:
                ny = y
                nx = x
                nh = hh+1
            elif i ==5:
                ny = y
                nx = x
                nh = hh-1

            if 0<=nh<h and 0<=ny<n and 0<=nx<m and bigMap[nh][ny][nx]!=-1:
                if visited[nh][ny][nx] == False:
                    # bigMap[nh][ny][nx]=bigMap[hh][y][x]+1
                    q.append((nh, ny, nx))
                    bigMap[nh][ny][nx]=bigMap[hh][y][x]+1
                    visited[nh][ny][nx] = True

                    
        #print(bigMap)
        #print()

total = 0
check = 0
for k in range(h):
    for j in range(n):
        
        total=max(max(bigMap[k][j]), total)
        #print(bigMap[k][j],'!', total)
        if 0 in bigMap[k][j]:
            check = 1
            print(-1)
            exit(0)
            break
if check ==0:
    print(total-1)




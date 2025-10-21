n = int(input())
d = list(input())
board  = [[[] for _ in range(n)] for _ in range(n)]

sy, sx = 0, 0
ny, nx = 0, 0

c2 = [[0], [1], [0, 1], [1, 0]] # '|'
c3 = [[2], [3], [2, 3], [3, 2]] # '-'

dy = [-1, 1, 0, 0] # 상, 하, 좌, 우 0, 1, 2, 3
dx = [0, 0, -1, 1]

# for i in range(n):
#     print(board[i])

# print()


def checkBoundary(y, x):
    if 0<=y<n and 0<=x<n:
        return 1
    else:
        return 0
    
for i in range(len(d)):
    if d[i]=='D':
        ny = dy[1]+sy
        nx = dx[1]+sx
        if checkBoundary(ny, nx):
            board[sy][sx].append(1)
            sy = ny
            sx = nx
            board[sy][sx].append(1)
            
    elif d[i]=='U':
        ny = dy[0]+sy
        nx = dx[0]+sx
        if checkBoundary(ny, nx):
            board[sy][sx].append(0)
            sy = ny
            sx = nx
            board[sy][sx].append(0)
    elif d[i]=='L':
        ny = dy[2]+sy
        nx = dx[2]+sx
        if checkBoundary(ny, nx):
            board[sy][sx].append(2)
            sy = ny
            sx = nx
            board[sy][sx].append(2)
    elif d[i]=='R':
        ny = dy[3]+sy
        nx = dx[3]+sx
        if checkBoundary(ny, nx):
            board[sy][sx].append(3)
            sy = ny
            sx = nx
            board[sy][sx].append(3)

# for i in range(n):
#     print(board[i])


for i in range(n):
    for j in range(n):
        board[i][j] = list(set(board[i][j]))
        if board[i][j] == []:
            board[i][j]= chr(46)
        elif board[i][j] in c2:
            board[i][j]= chr(124)
        elif board[i][j] in c3:
            board[i][j]= chr(45)
        else :
            board[i][j]=chr(43)
    
for i in range(n):
    print(''.join(map(str, board[i])))
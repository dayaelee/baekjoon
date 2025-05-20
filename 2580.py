import sys
input = sys.stdin.readline

mapp=[]
for i in range(9):
    mapp.append(list(map(int, input().split())))

zeros=[]
for ii in range(9):
    for jj in range(9):
        if mapp[ii][jj]==0:
            zeros.append((ii, jj))


def valid(y, x, num):
    for i in range(0, 9):
        if mapp[y][i]==num:
            return False
    for i in range(0, 9):
        if mapp[i][x]==num:
            return False
    
    sy=(y//3)*3
    sx=(x//3)*3

    for i in range(sy, sy+3):
        for j in range(sx, sx+3):
            if mapp[i][j]==num:
                return False
    return True

def backtrack(cnt):
    if cnt == len(zeros):
        for i in range(9):
            print(' '.join(map(str, mapp[i])))
        sys.exit(0)
    
    y, x = zeros[cnt]

    for i in range(1, 10):
        if valid(y, x, i):
            # print('?')
            mapp[y][x]=i
            backtrack(cnt+1)
            mapp[y][x]=0

if len(zeros)>=1:   
    backtrack(0)

for i in range(9):
    print(' '.join(map(str, mapp[i])))
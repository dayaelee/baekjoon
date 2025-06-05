import sys
input = sys.stdin.readline

base=[]
# 이동 방향 = 좌 하 우 상, 2칸 주기로 길이가 1씩 늘어남 
dy=[[0, 1], [0, -1], [0, 1], [0, -1]]
dx=[[-1, 0], [1, 0], [-1, 0], [1, 0]]

#좌, 하, 우, 상 (0 = 5%, 1-2 => 10%, 3-4 => 7%, 5-6=> 2%, 7-8 =>1%)
dyc=[[0, -1, 1, -1, 1, -2, 2, -1, 1], [2, 1, 1, 0, 0, 0, 0, -1, -1], [0, -1, 1, -1, 1, -2, 2, -1, 1], [-2, -1, -1, 0, 0, 0, 0, 1, 1]]
dxc=[[-2, -1, -1, 0, 0, 0, 0, 1, 1], [0, -1, 1, -1, 1, -2, 2, -1, 1], [2, 1, 1, 0, 0, 0, 0, -1, -1], [0, -1, 1, -1, 1, -2, 2, -1, 1]]

n=int(input())
for i in range(n):
    base.append(list(map(int, input().split())))

sy, sx = n//2, n//2

def calculate(num, ny, nx, minus, out):
    nminus = minus
    for i in range(9):
        ty=ny+dyc[num][i]
        tx=nx+dxc[num][i]
        if i == 0:
            if 0<=ty<n and 0<=tx<n:
                base[ty][tx]+=int(base[ny][nx]*0.05)
            else:
                out+=int(base[ny][nx]*0.05)
            nminus+=int(base[ny][nx]*0.05)
        elif 1<=i<=2:
            if 0<=ty<n and 0<=tx<n:
                base[ty][tx]+=int(base[ny][nx]*0.1)
            else:
                out+=int(base[ny][nx]*0.1)
            nminus+=int(base[ny][nx]*0.1)
        elif 3<=i<=4:
            if 0<=ty<n and 0<=tx<n:
                base[ty][tx]+=int(base[ny][nx]*0.07)
            else:
                out+=int(base[ny][nx]*0.07)
            nminus+=int(base[ny][nx]*0.07)
        elif 5<=i<=6:
            if 0<=ty<n and 0<=tx<n:
                base[ty][tx]+=int(base[ny][nx]*0.02)
            else:
                out+=int(base[ny][nx]*0.02)
            nminus+=int(base[ny][nx]*0.02)
        else:
            if 0<=ty<n and 0<=tx<n:
                base[ty][tx]+=int(base[ny][nx]*0.01)
            else:
                out+=int(base[ny][nx]*0.01)
            nminus+=int(base[ny][nx]*0.01)
    
    return out, nminus


def move(ssy, ssx, littleCnt, cnt, out):
    ny = ssy + dy[cnt][littleCnt]
    nx = ssx + dx[cnt][littleCnt]
    if (cnt ==0 or cnt == 2)and littleCnt==0:
        outResult, minus = calculate(0, ny, nx, 0, out)
    elif (cnt ==0 or cnt == 2)and littleCnt==1:
        outResult, minus = calculate(1, ny, nx, 0, out)
    elif (cnt ==1 or cnt == 3)and littleCnt==0:
        outResult, minus = calculate(2, ny, nx, 0, out)
    elif (cnt ==1 or cnt == 3)and littleCnt==1:
        outResult, minus = calculate(3, ny, nx, 0, out)
    
    ry = ny + dy[cnt][littleCnt]
    rx = nx + dx[cnt][littleCnt]
    if 0<=ry<n and 0<=rx<n:
        base[ry][rx] += base[ny][nx]-minus
    else:
        outResult+=base[ny][nx]-minus
    base[ny][nx]=0
    return ny, nx, outResult

def entire(sy, sx):
    cnt = 0
    dis= 1
    littleCnt = 0
    result = 0
    y, x = sy, sx
    while 1:
        while littleCnt<2:
            for i in range(dis):
                ny, nx, out = move(y, x, littleCnt, cnt%4, 0)
                result+=out
                y, x = ny, nx
                # print(y, x)
                # 종료 조건 
                if y==0 and x ==0:
                    return result
            littleCnt+=1
            
        cnt+=1
        littleCnt=0
        dis+=1
    return result



print(entire(sy, sx))
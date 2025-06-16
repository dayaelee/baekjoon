import sys
input = sys.stdin.readline
a=[]
n, m, k = map(int, input().split())
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(k):
    r, c, s = map(int, input().split())


# 가장 왼쪽 윗 칸 (r-s, c-s), 가장 오른쪽 아랫 칸(r+s, c+s)

sy, sx = r-s-1, c-s-1
ey, ex = r+s-1, c+s-1

def up(sy, sx, ex):
    keep = a[sy][ex]
    for i in range(ex, sx, -1):
        a[sy][i]=a[sy][i-1]
        print('hi', a[sy][i], a[sy][i-1])
        for i in range(n):
            print(a[i])
        print()
    return keep, a

def right(sy, ex, ey, keep):
    print('a', a)
    print('ey, ex', ey, ex)
    keep2 = a[ey][ex]
    for i in range(ey, sy, -1):
        a[i][ex]=a[i-1][ex]
    a[sy][ex]=keep
    return keep2, a

def down(ey, ex, sx, keep):
    keep2 = a[ey][sx]
    for i in range(sx, ex):
        a[ey][i]=a[ey][i+1]
    a[ey][ex]=keep
    return keep2, a

def left(ey, sx, sy, keep):
    for i in range(sy, ey):
        a[i][sx]= a[i+1][sx]
    a[ey][sx]=keep
    return a

for i in range(s): # 회전 행 수 
    keep, a = up(sy+i, sx+i, ex-i)
    keep, a = right(sy+i, ex-i, ey-i, keep)
    keep, a = down(ey-i, ex-i, sx+i, keep)
    a = left(ey-i, sx, sy+i, keep)

    if i ==0:
        for i in range(n):
            print(a[i])
        break
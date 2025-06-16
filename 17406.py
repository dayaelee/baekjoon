import sys
import itertools
import copy
input = sys.stdin.readline
originA=[]
n, m, k = map(int, input().split())
for i in range(n):
    originA.append(list(map(int, input().split())))

pocket=[]
for ii in range(k):
    pocket.append(list(map(int, input().split())))

# 가장 왼쪽 윗 칸 (r-s, c-s), 가장 오른쪽 아랫 칸(r+s, c+s)
case = list(itertools.permutations(pocket, len(pocket)))
# print(case)

result = float("inf")
for i in case:
    a=copy.deepcopy(originA)
    for j in i:
        r, c, s = j
        # print("j", j, 'r, s, c ', r, s, c )

        sy, sx = r-s-1, c-s-1
        ey, ex = r+s-1, c+s-1

        # print('sy, sx, ey, ex', sy, sx, ey, ex)

        def up(sy, sx, ex):
            # print('up')
            keep = a[sy][ex]
            for i in range(ex, sx, -1):
                a[sy][i]=a[sy][i-1]
                # print('hi', a[sy][i], a[sy][i-1])
            # for i in range(n):
            #     print(a[i])
            # print()
            return keep, a

        def right(sy, ex, ey, keep):
            # print('right')
            # print('ey, ex', ey, ex)
            keep2 = a[ey][ex]
            for i in range(ey, sy, -1):
                a[i][ex]=a[i-1][ex]
            a[sy+1][ex]=keep
            # for i in range(n):
            #     print(a[i])
            # print()
            return keep2, a

        def down(ey, ex, sx, keep):
            # print('down')
            keep2 = a[ey][sx]
            for i in range(sx, ex):
                a[ey][i]=a[ey][i+1]
            a[ey][ex-1]=keep
            # for i in range(n):
            #     print(a[i])
            # print()
            return keep2, a

        def left(ey, sx, sy, keep):
            # print('left')
            for i in range(sy, ey):
                a[i][sx]= a[i+1][sx]
            a[ey-1][sx]=keep
            # for i in range(n):
            #         print(a[i])
            return a


        for i in range(s): # 회전 행 수 
            keep, a = up(sy+i, sx+i, ex-i)
            keep, a = right(sy+i, ex-i, ey-i, keep)
            keep, a = down(ey-i, ex-i, sx+i, keep)
            a = left(ey-i, sx+i, sy+i, keep)

            # print('good')
            # for i in range(n):
            #     print(a[i])
        
    tmpR=float('inf')
    for rr in range(len(a)):
        tmpR = min(tmpR, sum(a[rr]))

    
    result = min(result, tmpR)

print(result)
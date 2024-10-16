
import sys
input = sys.stdin.readline

mapp= []
n, m = map(int, input().split())
for i in range(n):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)


t3x = [[1, 0, 1], [0, 1, -1]], [[0, -1, +1], [1, 0, 1]], [[0, 1, -1], [1, 0, 1]], [[0, 1, 0], [1, 0, 1]], [[-1, 0, -1], [0, 1, 0]],[[0, -1, 0],[1, 0, 1]],[[1, 0, 1],[0, 1, 0]], [[1, 0, 1],[0, 1, -1]],[[1, 0, 1],[0, -1, 1]], [[0,0,1], [1, 1, 0]], [[0, 1, 1], [1, -1, 0]], [[1, 0, 0], [0, 1, 1]],[[0, -1, -1], [1, 0, 0]],[[0, 1, 1], [1, 0, 0]], [[1, -1, 0], [0, 1, 1]], [[1, 1, 0], [0, 0, 1]], [[0, 0, -1], [1, 1, 0]], [[1, 1, 1], [0, 0, 0]], [[0, 0, 0],[1, 1, 1]], [[1, 0, -1], [0, 1, 0]]

result = 0
for i in range(n):
    for j in range(m):
        for indexx, value in enumerate(t3x):
            xx, yy = value
            
            summ = mapp[i][j]
            clear=0
            nx = j
            ny = i
            for index in range(3):
                ni = ny + yy[index]
                nj = nx + xx[index]

                if 0<=ni<n and 0<=nj<m:
                    summ+=mapp[ni][nj]
                    ny = ni
                    nx = nj
                else:
                    clear=1
                    break
            
            if clear ==0:
                if result< summ:
                    result=summ

print(result)
            


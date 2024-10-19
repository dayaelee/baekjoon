import sys
input = sys.stdin.readline
from collections import deque
import itertools
import copy

dy=[1, -1, 0, 0]
dx=[0, 0, 1, -1]

n, m = map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

pickme=[]
whereTwo = deque()
for i in range(n):
    for j in range(m):
        if mapp[i][j]==0:
            pickme.append([i, j])
        elif mapp[i][j]==2:
            whereTwo.append([i,j])
combi = itertools.combinations(pickme, 3)

maxx=0

for index, i in enumerate(combi):
    mappTmp = copy.deepcopy(mapp)
    whereTwoTmp = copy.deepcopy(whereTwo)
    for check in i:
        y, x = check
        mappTmp[y][x]=1
    
    while whereTwoTmp:
        yy, xx= whereTwoTmp.popleft()
        
        for k in range(4):
            yyy = dy[k]+yy
            xxx = dx[k]+xx

            if 0<=yyy<n and 0<=xxx<m and mappTmp[yyy][xxx]==0:
                mappTmp[yyy][xxx]=2
                whereTwoTmp.append([yyy, xxx])

    cnt=0
    for ii in range(n):
        for jj in range(m):
            if mappTmp[ii][jj] == 0:
                cnt+=1

    if maxx<cnt:
        maxx=cnt
        
print(maxx)
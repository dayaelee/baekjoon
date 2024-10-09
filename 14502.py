'''
바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고
연구소는 크기가 N×M인 직사각형으로
연구소는 빈 칸, 벽

일부 칸은 바이러스가 존재
이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 

새로 세울 수 있는 벽의 개수는 3개
꼭 3개를 세워야 한다.

0은 빈 칸, 1은 벽, 2는 바이러스

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
위의 지도에서 안전 영역의 크기는 27이다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값

'''

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

'''
0인 칸을 모두 모아서
3개를 뽑는다. 
그리고 나머지 2의 위치를 다 찾아서 
2가 갈수있는 곳은 모두 체크한다. 

그리고 최종적으로 안전영역을 센다. 
'''
pickme=[]
whereTwo = deque()
for i in range(n):
    for j in range(m):
        if mapp[i][j]==0:
            pickme.append([i, j])
        elif mapp[i][j]==2:
            whereTwo.append([i,j])
#print('wheretwo', whereTwo)
#[0, 4], [1, 3], [3, 3]
combi = itertools.combinations(pickme, 3)

maxx=0

for index, i in enumerate(combi):
    #print(index, i)
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
                #print(yyy, xxx)
                mappTmp[yyy][xxx]=2
                #print('mappTmp[yyy][xxx]=2', mappTmp[yyy][xxx])
                whereTwoTmp.append([yyy, xxx])
                #print('hi', whereTwo)

    

    cnt=0
    for ii in range(n):
        for jj in range(m):
            if mappTmp[ii][jj] == 0:
                cnt+=1

    if maxx<cnt:
        maxx=cnt
        #print('maxx', cnt)
        
        

print(maxx)
    

    




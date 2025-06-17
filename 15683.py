'''
1번 CCTV는 한 쪽 방향만 감시할 수 있다. 

2번과 3번은 두 방향을 감시할 수 있는데, 
2번은 감시하는 방향이 서로 반대방향이어야 하고, 
3번은 직각 방향이어야 한다. 

4번은 세 방향, 
5번은 네 방향을 감시


CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시, 벽X
CCTV가 감시할 수 없는 영역은 사각지대

CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향, 대각선 X
0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호
CCTV는 CCTV를 통과할 수 있다.

CCTV의 방향을 적절히 정해서
사각 지대의 최소 크기를 구하는 프로그램
'''

import sys
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy=[
    [[1], [-1], [0] , [0]], 
    [[0, 0], [-1, 1]], 
    [[-1, 0], [1, 0], [1, 0], [-1, 0]], 
    [[0, -1, 0], [-1, 0, 1], [-1, 0, 1], [0, 1, 0]], 
    [[-1, 1, 0, 0]]] 
dx=[
    [[0], [0], [-1], [1]], # 1
    [[-1, 1], [0, 0]], # 2 
    [[0, 1], [0, 1], [0, -1], [0, -1]], # 3
    [[-1, 0, 1], [0, 1, 0], [0, -1, 0], [-1, 0, 1]], # 4
    [[0, 0, -1, 1]]] # 5


n, m = map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))


def findC(mapp):
    cctvs=[]
    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if 1<=mapp[i][j]<6:
                cctvs.append((i, j, mapp[i][j]))
    return cctvs

def check(y, x, dirY, dirX, tmp): # 시선 처리 
    q = deque([(y, x)])
    while q:

        yy, xx = q.popleft()

        ny = yy + dirY
        nx = xx + dirX

        if 0<=ny < n and 0<= nx < m and tmp[ny][nx]!=6:
            if tmp[ny][nx]==0:
                tmp[ny][nx]=-1
            q.append((ny, nx))

    print()

    return tmp

def findZero(tmp):
    check = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                check+=1
    return check 

    

def backtrack(cMap, start, mapp, count):
    global result 
    if start == len(cMap):
        result = min(count, result)
        return 
    # cctv 순회 
    y, x, num = cMap[start]
    num-=1
    case = len(dy[num])
    for j in range(case): # 각 cctv에서 가능한 감시 방법 순회
        print('hi', dy[num][j], dx[num][j])
        case2 = len(dy[num][j])
        
        ntmp = copy.deepcopy(mapp)
        for dir in range(case2): # 케이스에 대한 세부 계산
            ntmp = check(y, x, dy[num][j][dir], dx[num][j][dir], ntmp)
        cnt = findZero(ntmp)
        backtrack(cMap, start+1, ntmp, cnt)
        result = min(cnt, result)
        print()
        print('this is i', i)
        for kk in range(len(ntmp)):
            print('c ', ntmp[kk])
        

result = float('inf')
cMap = findC(mapp)
if cMap:
    backtrack(cMap,0, mapp, float('inf'))
    print(result)
else:
    result = 0
    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if mapp[i][j]==0:
                result +=1
    print(result)


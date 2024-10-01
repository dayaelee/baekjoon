'''
로봇 청소기 
'''
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
startY, startX, dir = map(int, input().split())
mapp = []
for i in range(n):
    mapp.append(list(map(int, input().split())))

dx=[0, -1, 0, 1] # 북 서 남 동
dy=[-1, 0, 1, 0] # 북쪽을 y, x 기준 1, 0으로 표기해서 틀렸음 ....... 정신차려!! 

'''
1. 현재 칸이 청소되지 않은 경우, 청소
2. 주변 4칸중 모든 칸이 청소된 경우 => 청소가 필요없는 경우 
    -> 바라보는 방향 유지한 채로 한칸 후진 하고 1번
    -> 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없으면 작동 중지
3. 주변 4칸중 청소할 칸이 있는 경우, 
    1. 반시계 방향으로 90도 회전
    2. 바라보는 방향 기준으로 앞칸이 청소되지 않은 빈 칸인 경우 한칸 전진
    3. 1번으로 돌아감 

0 청소가 되지 않은 빈 칸
1 벽이 있는 것 
'''

def solutions(x, y, dir):
    cnt = 0 # 청소하는 칸의 개수 
    while 1:
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if mapp[y][x] == 0:
            mapp[y][x]=9
            cnt+=1

        check = 0 # 주변 4칸이 모두 청소된 칸인지 확인용 1은 청소필요, 1은 청소 불필요 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if mapp[ny][nx]==0:
                #청소 필요한 칸 발견
                check =1
                break
            
        if check == 1:
            # 반시계 방향으로 90도 회전
            dir=dir+1
            if dir==4:
                dir = 0
            sx=x+dx[dir]
            sy=y+dy[dir]
            
            if mapp[sy][sx]==0:
                # 전진함 
                x = sx
                y = sy
        
        # 청소가 필요 없는 경우 
        if check ==0:
            nny = y-dy[dir]
            nnx = x-dx[dir]
            
            if mapp[nny][nnx]==1:
                return cnt
            else:
                x=nnx
                y=nny

if dir ==1:
    dir = 3
elif dir ==2:
    dir =2
elif dir == 3:
    dir = 1
print(solutions(startX, startY, dir))
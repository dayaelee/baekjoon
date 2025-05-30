import sys
import math
from collections import deque
input = sys.stdin.readline

dy=[-1, -1, 0, 1, 1, 1, 0, -1] # 0, 1, 2, 3, 4, 5, 6, 7
dx=[0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
balls=[]
for i in range(m):
    balls.append(list(map(int, input().split())))

mapp=[[[] for _ in range(n+1)] for _ in range(n+1)]

#파이어볼 위치 체크
for i in range(m): 
    r, c, mm, s, d=balls[i]
    mapp[r][c].append([r, c, mm, s, d])

def move(basket):
    bag=[]
    for i in range(len(basket)):
        r, c, mm, s, d=basket[i]
        
        q = deque(mapp[r][c])
        if q:
            q.popleft()
            mapp[r][c]=list(q)
        
        nr = (r + (dy[d] * s))%n 
        if nr==0:
            nr=n
        nc = (c + (dx[d] * s))%n
        if nc==0:
            nc=n

        mapp[nr][nc].append([nr, nc, mm, s, d])
        bag.append([nr, nc, mm, s, d])
    return bag

def check2Over(mapp):
    box=[]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if len(mapp[i][j])==1:
                i, j, nm, ns, dd= mapp[i][j][0]
                box.append([i, j, nm, ns, dd])
            elif len(mapp[i][j])>=2:
                sumMM=0
                sumS=0
                sumCnt=len(mapp[i][j])
                hFlag, zFlag=1, 1
                for f in mapp[i][j]:
                    r, c, mm, s, d = f
                    sumMM+=mm
                    sumS+=s
                    if zFlag==1 and d%2!=0:
                        zFlag=0
                    
                    if hFlag==1 and d%2==0:
                        hFlag=0
                    
                nm= math.floor(sumMM/5)
                ns= math.floor(sumS/sumCnt)
                
                mapp[i][j]=[]
                if nm!=0:
                    if hFlag==1 or zFlag==1:
                        for dd in range(0, 7, 2):
                            box.append([i, j, nm, ns, dd])
                            mapp[i][j].append([i, j, nm, ns, dd])
                    else:
                        for dd in range(1, 8, 2):
                            box.append([i, j, nm, ns, dd])
                            mapp[i][j].append([i, j, nm, ns, dd])

    return box            


def sumM(target):
    total=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for mm in mapp[i][j]:
                total+=mm[2]

    return total

for kk in range(k):
    bag = move(balls)
    mapp=[[[] for _ in range(n+1)] for _ in range(n+1)]
    #파이어볼 위치 체크
    for i in range(len(bag)): 
        r, c, mm, s, d=bag[i]
        mapp[r][c].append([r, c, mm, s, d])
    balls=check2Over(mapp)

    if not balls:
        balls=bag

print(sumM(balls))

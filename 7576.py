from collections import deque

import sys
input = sys.stdin.readline

dx =[0, 0, 1, -1]
dy =[1, -1, 0, 0]


m, n = map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

total = n*m
totalbabyTomato=0
totaladultTomato=0
noTomato=0

queue = deque()

for i in range(n):
    for j in range(m):
        if mapp[i][j]==0:
            totalbabyTomato+=1
        elif mapp[i][j]==1:
            totaladultTomato+=1
            queue.append([(i, j), 0])
        elif mapp[i][j]==-1:
            noTomato+=1

totalTomato = total-noTomato

def solution(totalTomato, totaladultTomato, queue):
    if totalTomato == totaladultTomato:
        return 0
    else:
        growth =0
        while queue:
            where, day = queue.popleft()

            y, x = where

            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]

                if ny<0 or nx<0 or ny>=n or nx>=m or mapp[ny][nx]==-1 or mapp[ny][nx]==1:
                    continue

                mapp[ny][nx]=1
                growth+=1
 
                queue.append([(ny, nx), day+1])

        if totalbabyTomato== growth:
            return day
        elif totalbabyTomato>growth:
            return -1
        
        

print(solution(totalTomato, totaladultTomato, queue))

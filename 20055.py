import sys
from collections import deque
input =sys.stdin.readline

n, k = map(int, input().split())
e = list(map(int, input().split())) # 0은 안씀
robot = [0] * n

ans = 0

while 1:
    ans +=1

    e = [e[-1]]+e[:-1] # 컨베이어 벨트 회전
    robot = [0]+robot[:-1] # 로봇 회전 
    robot[n-1]=0 # 마지막꺼는 내려줌 
    print('')
    for i in range(n-2, 0, -1):
        print('i', i)
        if robot[i]==1 and robot[i+1]==0 and e[i+1]>0:
            robot[i], robot[i+1] = 0, 1
            e[i+1]-=1

    if e[0]>0:
        robot[0]=1
        e[0]-=1

    if e.count(0)>=k:
        break
print(ans)
    
    



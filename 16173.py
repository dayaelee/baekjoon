'''
정사각형
구역 외부로 나가면 패배
좌측 상단에서 출발

도착점 n-1, n-1

한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼
'''
from collections import deque
# 오른쪽과 아래
dy=[0, 1]
dx=[1, 0]

n = int(input())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

# visited=[[False for _ in range(n)] for _ in range(n)]
#print(visited)

def bfs(y, x, lenn):
    queue= deque([(y, x, lenn)])
    check = 0
    while queue:
        
        y, x, length = queue.popleft()
        

        if y==n-1 and x==n-1:
            #print('????y, x', y, x)
            return True

        #print('y, x, length', y, x, length)
        
        for i in range(2):
            
            ny = y + (dy[i] * length)
            nx = x + (dx[i] * length)
            #print('hi, ny, nx, length', ny, nx, length)
            if 0<=ny<n and 0<=nx<n:
                if ny==n-1 and nx==n-1:
                    return True
                else:
                    if mapp[ny][nx]>0:
                        Nlength = mapp[ny][nx]
                        # mapp[ny][nx]=-1
                        queue.append((ny, nx, Nlength))
                    

    
    return False
        
if bfs(0, 0, mapp[0][0])==False:
    print('Hing')
else:
    print("HaruHaru")
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dy=[0, -1, -1, -1, 0, 1, 1, 1]
dx=[-1, -1, 0, 1, 1, 1, 0, -1]

dy2=[-1, -1, 1, 1]
dx2=[-1, 1, -1, 1]

a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
orders=[]
for i in range(m):
    d, s = map(int, input().split())
    orders.append([d, s])

def fstCloud(n):
    n-=1
    return [[n, 0], [n, 1], [n-1, 0], [n-1, 1]]

def move(cloud, now, orders):
    ncloud = cloud
    
    dir, s = orders[now]# 방향, 거리
    dir -=1
    newCloud=[]
    for j in ncloud:
        y, x = j
        ny, nx = (y+ (dy[dir]*s))%n, (x+ (dx[dir]*s))%n
        newCloud.append([ny, nx])
    ncloud = newCloud

    return ncloud

def rainDrop(ncloud, a):
    for i in ncloud:
        y, x =i
        a[y][x]+=1
    return ncloud, a

def vivaragy(upWater):
    upWater.sort(key = lambda x: (x[0]))
    for i in range(len(upWater)):
        y, x = upWater[i]
        cnt = 0
        for j in range(4):
            ny = y + dy2[j]
            nx = x + dx2[j]

            if 0<=ny<n and 0<=nx<n and a[ny][nx]>0:
                cnt+=1
        a[y][x]+=cnt
    return upWater

def makeCloud(nowCloud):
    visited=[[False]*n for _ in range(n)]
    for i in nowCloud:
        y, x = i
        visited[y][x]=True


    newCloud=[]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                if a[i][j]>=2:
                    a[i][j]-=2
                    newCloud.append([i, j])
    return newCloud
    
def calSum():
    answer = 0
    for i in range(n):
        for j in range(n):
            if a[i][j]>0:
                answer+=a[i][j]
    return answer

def start(a):
    repeat = len(orders)
    now = 0
    while now<repeat:
        if now ==0:
            cloud = fstCloud(n)
        else:
            cloud = newCloud
        ncloud=move(cloud, now, orders)
        upWater, a = rainDrop(ncloud, a)
        # cloud 모두 사라짐
        nowCloud = vivaragy(upWater)
        newCloud = makeCloud(nowCloud)
        now+=1
    print(calSum())
start(a)
    

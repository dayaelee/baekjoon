from collections import deque
import sys
input = sys.stdin.readline


def bfs(sy, sx):
    q=deque([(sy, sx)])
    visited=[False]*(n+1)

    while q:
        #print(q)
        y, x = q.popleft()

        if y == ry and x == rx:
            print("happy")
            return 

        for i in range(len(p)):
            dy, dx=p[i]
            if (abs(dy-y) + abs(dx-x)) //50 ==20 and (abs(dy-y) + abs(dx-x)) %50 ==0 and visited[i]==False:
                visited[i] = True
                q.append((dy, dx))
            elif (abs(dy-y) + abs(dx-x)) //50 <20 and visited[i]==False:
                visited[i] = True
                q.append((dy, dx))
    return print("sad")



t = int(input())
for i in range(t):
    n = int(input())
    p=[]
    for j in range(n+2):
        if j == 0:
            gy, gx = map(int, input().split())
        elif j == n+1:

            ry, rx = map(int, input().split())
            p.append((ry, rx))
        else:
            p.append(list(map(int, input().split())))

    bfs(gy, gx)

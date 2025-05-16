from collections import deque
a, b = map(int, input().split())

def bfs(start):
    q = deque([(start, 0)])

    while q:
        value, cnt = q.popleft()

        if value == b:
            print(cnt+1)
            exit()
        elif value <b:
            q.append((value*2, cnt+1))
            q.append((int(str(value)+'1'), cnt+1))

bfs(a)
print(-1)
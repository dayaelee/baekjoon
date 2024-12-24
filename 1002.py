import sys
import math
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, (input().split()))

    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if dis == 0 and r2==r1:
        print(-1)
    elif dis == abs(r2-r1) or r2+r1==dis:
        print(1)
    elif abs(r2-r1) < dis < r2+r1:
        print(2)
    else:
        print(0)
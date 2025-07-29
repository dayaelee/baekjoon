import sys
input = sys.stdin.readline

from collections import deque
n = int(input())
listt = deque([i for i in range(1, n+1)])

# print(listt)
bag = []
for i in range(n-1):
    # print(listt)
    bag.append(listt.popleft())
    value = listt.popleft()
    listt.append(value)

print(' '.join(map(str, bag+list(listt))))

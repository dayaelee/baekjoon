import sys
input = sys.stdin.readline
n, m = map(int, input().split())
total = []
for i in range(n):
    total.append(int(input()))
total.sort()
global minn
minn = sys.maxsize

start = 0
end = 1
while end < n:
    diff = total[end]-total[start]
    if diff > m:
        minn = min(minn, diff)
        start+=1
    elif diff == m:
        minn = m
        break
    else:
        end+=1

print(minn)
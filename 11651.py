import sys
input = sys.stdin.readline
n = int(input())
tmp = []

for i in range(n):
    tmp.append(list(map(int, input().split())))

tmp.sort(key=lambda x: x[0])
tmp.sort(key=lambda x: x[1])
for i in tmp:
    print(' '.join(map(str, i)))

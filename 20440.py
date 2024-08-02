import sys
from collections import defaultdict
input = sys.stdin.readline

n=int(input())
dict = defaultdict(int)

for i in range(n):
    # 입장시간, 퇴장시간
    e, x = map(int, input().split()) 

    dict[e] += 1
    dict[x] -= 1
    

maxx, nowMos = 0, 0
startTime, endTime = 0, 0
flag = False
for i in sorted(dict.keys()):
    nowMos += dict[i]

    if nowMos > maxx:
        maxx = nowMos
        startTime = i
        flag = True
    elif  nowMos < maxx and nowMos - dict[i] == maxx and flag:
        flag = False
        endTime = i

print(maxx)
print(startTime, endTime)
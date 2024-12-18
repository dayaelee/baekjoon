
import sys
input = sys.stdin.readline
n = int(input())

tmp=[]
rank=[]

for i in range(n):
    value = list(map(int, input().split()))
    value.append(1)
    tmp.append(value)

for index, i in enumerate(tmp):
    kg, cm, cnt = i
    for j in tmp:
        jkg, jcm, jcnt = j
        if kg< jkg and cm< jcm:
            tmp[index][2]+=1
    rank.append(tmp[index][2])

print(' '.join(map(str, rank)))


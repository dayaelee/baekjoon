'''


서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다. 

'''
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, input().split())))

    tmp.sort()
    #print(tmp)
    standard = tmp[0][1]
    cnt = 1
    for j in range(1, len(tmp)):
        if standard>tmp[j][1]:
            standard=tmp[j][1]
            cnt+=1
    print(cnt)

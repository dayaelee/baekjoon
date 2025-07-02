import sys, itertools
input = sys.stdin.readline

n = int(input())
tmp =[]
for i in range(n):
    v = int(input())
    tmp.append(v)

# print(max(len(tmp)*min(tmp), e))
answer  = min(tmp)

tmp.sort()
for i in range(n):
    answer=max(tmp[i]*(n-i), answer)
print(answer)
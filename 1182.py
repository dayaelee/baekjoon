import itertools
n, s = map(int, input().split())
tmp = list(map(int, input().split()))

cnt = 0
for i in range(1, len(tmp)+1):
    check = list(itertools.combinations(tmp, i))
    for j in check:
        result = sum(j)
        if s==result:
            cnt+=1
print(cnt)
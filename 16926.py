import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

def up(sn, en, sm, em):
    min=mapp[sn][sm]
    if m>=1:
        for i in range(sm+1, em):
            mapp[sn][i-1]=mapp[sn][i]
    return left(min, sn, en, sm, em)

def left(min, sn, en, sm, em):
    min2 = mapp[en-1][sn]
    if n>=1:
        for i in range(en-1, sn, -1):
            mapp[i][sn]=mapp[i-1][sm]
    mapp[sn+1][sn]=min
    return down(min2, sn, en, sm, em)

def down(min, sn, en, sm, em):
    max = mapp[en-1][em-1]
    if m>=1:
        for i in range(em-1, sn, -1):
            mapp[en-1][i]=mapp[en-1][i-1]
    mapp[en-1][sn+1]=min
    return right(max, sn, en, sm, em)

def right(max, sn, en, sm, em):
    min = mapp[sn][em-1]
    if n>=1:
        for i in range(sn+1, en):
            mapp[i-1][em-1]=mapp[i][em-1]
    mapp[en-2][em-1]=max
    return min

for j in range(r):
    for i in range(min(n//2, m//2)):
        up(i, n-i, i, m-i)

for i in range(n):
    print(' '.join(map(str, mapp[i])))
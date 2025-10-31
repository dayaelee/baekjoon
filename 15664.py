n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

b=[]
def backtrack(tmp, now, cnt):
    if cnt == m:
        print(' '.join(map(str, tmp)))
        return

    prev = 0
    for i in range(now, len(a)):
        if a[i] != prev:
            tmp.append(a[i])
            prev = a[i]
            backtrack(tmp, i+1, cnt+1)
            tmp.pop()

backtrack([], 0, 0)

import collections
a = collections.defaultdict(int)

n, p, q = map(int, input().split())

a[0]=1

def dp(i, p, q):
    if a[i] != 0:
        return a[i]
    a[i] = dp(int(i/p), p, q) + dp(int(i/q), p, q)
    return a[i]

print(dp(n, p, q)) 
import math
n = int(input())

def is_prime_number(x):
    if x ==1:
        return False
    xx= int(math.isqrt(x))
    for i in range(2, xx+1):
        if x%i==0:
            return False
    return True

def dfs(now, depth, n):
    if depth == n:
        print(now)
        return
    for d in (1, 3, 7, 9):
        next = now*10 + d
        if is_prime_number(next):
            dfs(next, depth+1, n)

for k in (2, 3, 5, 7):
    dfs(k, 1, n)
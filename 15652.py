import itertools
n, m = map(int, (input().split()))

tmpList = [i for i in range(1, n+1)]

tmp = list(itertools.combinations_with_replacement(tmpList, m))

print(tmp)

for i in tmp:
    print(' '.join(map(str, i)))

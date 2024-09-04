from itertools import combinations, permutations

n = int(input())

tmpList=list(range(n))

perm = list(combinations(tmpList, 2))

print(len(perm)*2)


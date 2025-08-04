n, k = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
print(nlist[k-1])

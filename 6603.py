import itertools
import sys
input=sys.stdin.readline
while 1:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    else:
        n = a[0]
        nList = [a[i] for i in range(1, len(a))]
        tmp = sorted(list(itertools.combinations(nList, 6)), reverse=True)
        for i in range(len(tmp)-1, -1, -1):
            print(' '.join(map(str, tmp[i])))
        print('')

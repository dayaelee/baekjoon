os, om = map(int, input().split())
ts, tm = map(int, input().split())

bm=om*tm
bs= (os*tm) + (om*ts)

def gdc(bs, bm):
    while bm:
        bs, bm = bm, bs % bm 
    return bs

tmp = gdc(bs, bm)

if tmp==1:
    print(bs, bm)
else:
    print(bs//tmp, bm//tmp)



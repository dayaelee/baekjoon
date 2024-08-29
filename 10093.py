s, e = map(int, input().split())
tmp=[]
if s<=e:
    for i in range(s+1, e):
        tmp.append(str(i))
    if tmp:
        print(len(tmp))
        print(' '.join(tmp))
    else:
        print(0)
else:
    for i in range(e+1, s):
        tmp.append(str(i))
    if tmp:
        print(len(tmp))
        print(' '.join(tmp))
    else:
        print(0)

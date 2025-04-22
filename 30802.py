n = int(input())
tsize = list(map(int, input().split()))
t, p = map(int, input().split())
tresult=0
for i in range(6):
    if tsize[i]%t>0:
       tresult+=((tsize[i]//t) +1)
    elif tsize[i]%t==0:
        tresult+=(tsize[i]//t)
print(tresult)
presult=0
print(n//p, n%p)

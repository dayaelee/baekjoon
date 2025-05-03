n = int(input())
if n ==0:
    print(0)
else:
    a=[]
    for i in range(n):
        a.append(int(input()))

    if n ==1:
        print(a[0])
    else:
        a.sort()
        p=len(a)/100*15
        tmp=p
        if tmp - int(tmp)>=0.5:
            p=int(tmp)+1
        else:
            p=int(tmp)
        if p>=1:
            resulta=a[int(p):-p]
            target=sum(resulta)/len(a[int(p):-p])
        else:
            target=sum(a)/len(a)
        if target-int(target)>=0.5:
            target=int(target)+1
        else:
            target=int(target)
        print(target)
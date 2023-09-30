n, k = map(int,input().split())

llist=[]

for i in range(1, n+1):
    if (n%i==0):
        llist.append(i)


if(len(llist)>=k):
    print(llist[k-1])
else:
    print(0)


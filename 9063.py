n = int(input())


llist = list()

for i in range(0, n):
    tmp =[]
    for j in range(0, 2):
        tmp.append(0)
    llist.append(tmp)

minx=0
maxx=0
miny=0
maxy=0

for i in range(0, n):
    llist[i][0], llist[i][1] = map(int, input().split(" ")) 
    if i==0:
        minx=llist[i][0]
        maxx=llist[i][0]
        miny=llist[i][1]
        maxy=llist[i][1]
    else:
        if(minx>llist[i][0]):
            minx=llist[i][0]

        if(maxx<llist[i][0]):
            maxx=llist[i][0]
        
        if(maxy<llist[i][1]):
            maxy=llist[i][1]
        
        if(miny>llist[i][1]):
            miny=llist[i][1]
    print("minx",minx)
    print("maxx",maxx)
    print("miny",miny)
    print("maxy",maxy)

print(*llist)



# 크기 순으로 출력하면 됨

if n==1:
    print(0)
else:
    print((maxx-minx)*(maxy-miny))

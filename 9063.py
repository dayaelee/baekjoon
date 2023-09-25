n = int(input())


llist = list()

for i in range(0, n):
    tmp =[]
    for j in range(0, 2):
        tmp.append(0)
    llist.append(tmp)

for i in range(0, n):
    llist[i][0], llist[i][1] = map(int, input().split(" ")) 

print(*llist)

hx, lx, hy, ly = 0


# 크기 순으로 출력하면 됨 

if n>1:
    for i in range(0, n):
        if i == 0:
            
            llist[i][0]
else:
    pass
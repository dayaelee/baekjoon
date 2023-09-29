n = int(input())
llist=[]
for i in range(0,n):
    llist.append(0)
    llist[i]=int(input())

llist.sort()

for i in range(0,n):
    print(llist[i])
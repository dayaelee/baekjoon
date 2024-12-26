import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    listOri = list(map(int, input().split()))
    listOriReal=[]
    target = listOri[m]

    for k in range(len(listOri)):
        listOriReal.append([listOri[k], k])
        listOri[k]=[listOri[k], k]
    visited=[False for _ in range(len(listOri))]
    cnt=0
    listOri.sort(reverse=True)
    orderList=[]
    for k in range(len(listOri)):
        orderList.append(listOri[k][0])
    realcheck=0
    j=0
    while 1:
        if orderList[j] == listOriReal[cnt][0] and visited[cnt]==False:
            visited[cnt]=True
            
            realcheck+=1
            if target == orderList[j] and cnt ==m:
                print(realcheck)
                break
            
            j+=1
            
        else: 
            cnt+=1
            if cnt==len(listOri):
                cnt=0
                
                

    

import sys 
input = sys.stdin.readline

n = int(input())
tmp = []
for i in range(n):
    tmp.append(list(map(int, input().split())))
visited=[False] * 501
tmp.sort(key = lambda x: -x[0])
#print(tmp)
cnt = 0
for i in tmp:
    a, b = i
    
    if a==b:
        if visited[a]==False:
            visited[a]=True
            cnt+=1
    else:
        if a>b:
            check = 0
            for j in range(a, b, -1):
                if visited[j]==False:
                    continue
                else:
                    check = 1
                    
                    #print('cnt', cnt)
                    break
            if check == 0:
                #print(i)
                cnt+=1
                for jj in range(a, b, -1):
                    visited[jj]=True
        else:
            check = 0
            for j in range(a, b+1):
                if visited[j]==False:
                    continue
                else:
                    check = 1
                    
                    #print('cnt', cnt)
                    break
            if check == 0:
                #print(i)
                cnt+=1
                for jj in range(a, b+1):
                    visited[jj]=True
print(n-cnt) 



n = int(input())

'''
사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. 
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.

1 2 3 4

2 1 1 0

4 2 1



'''

tmp = list(map(int, input().split()))

visited = [False for _ in range(n)]

result = []


cnt = 0
restart = 0

'''
1 2 3 4

2 1 1 0
'''
while 1:
    if len(result)==n:
        break
    
    for i, value in enumerate(tmp):
        if restart == 0:
            if value == 0:
                result.append(i+1)
                #print('ho', result)
                visited[i]=True
                restart = 1
                cnt+=1
                break
            else:
                    if result:
                        check = 0
                        for j in result:
                            if j >= i+1:
                                check +=1
                        
                        if check == value:
                            result.append(i+1) 
        else:
            if value == 0 and visited[i]==False:
                result.append(i+1)
                visited[i]=True
                break
            else:
                if visited[i]==False:
                    if result:
                        check = 0
                        for j in result:
                            if j >= i+1:
                                #print('j', j, i+1)
                                check +=1
                                
                        
                        if check == value:
                            result.append(i+1)
                            visited[i]=True
                            break
hi = " ".join(map(str,result))                      
print(hi)
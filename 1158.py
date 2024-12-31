from collections import deque 
n, k = map(int, input().split())

tmp = [ i for i in range(1, n+1)]

tmp = deque(tmp)
cnt = 1
result =[]
#1, 2, 4, 5, 7   /   3, 6
while tmp:
    
    if cnt == k:
        
        value = tmp.popleft()
        # print(value)
        result.append(value)
        cnt=1
    else:
        value = tmp.popleft()
        tmp.append(value)
        cnt+=1
#     print(tmp, 'cnt:', cnt)

# print(cnt)
# print(result)
    
print('<'+', '.join(map(str, result))+'>')
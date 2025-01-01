from collections import deque
n, k = map(int, input().split())

tmp = [i for i in range(1, n+1)]

tmp = deque(tmp)

result = []
cnt = 1
while tmp:
    if cnt == k:
        value = tmp.popleft()
        result.append(value)
        cnt=1
    elif cnt < k:
        value = tmp.popleft()
        tmp.append(value)
        cnt+=1
print('<'+', '.join(map(str, result))+ '>')





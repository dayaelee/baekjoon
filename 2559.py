from collections import deque
n, k = map(int, input().split())
tmp = list(map(int, input().split()))
k=k-1
answer = -10000000
start = 0
end = k
basket=deque([])
sum = 0
for i in range(len(tmp)-k):
    #print(i, i+k)
    
    if i ==0:
        for j in range(0, k+1):
            basket.append(tmp[j])
            sum+=tmp[j]
        start+=1
        end+=1
    else:
        value=basket.popleft()
        sum-=value
        basket.append(tmp[end])
        sum+=tmp[end]
        start+=1
        end+=1
    #print(basket)
    answer=max(sum, answer)

print(answer)

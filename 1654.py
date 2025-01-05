k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start = 1
end = max(arr)


while start <= end :
    mid = (start+end) // 2
    
    sum = 0
    for cable in arr :
        sum += (cable // mid)
    
    if sum < n : #나온 선이 너무 적으면 
        end = mid - 1 
    else : #나온 선이 너무 많으면 
        start = mid + 1
        
    
print(end)
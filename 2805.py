n, m = map(int, input().split())
heights = list(map(int, input().split()))

end = max(heights)
start = 1

def makeCnt(start, end, result):
    if result > m:
        start = ((start + end)//2)+1
    elif result < m:
        end = ((start + end)//2)-1

    return start, end, (start + end) // 2

cnt = (start + end) // 2

while start<end:
    result = 0
    for i in range(n):
        if heights[i] >= cnt:
            result += heights[i] - cnt
    if result == m:
        
        break
    else:
        start, end, cnt = makeCnt(start, end, result)
print(cnt)
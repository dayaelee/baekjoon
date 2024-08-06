import sys
input = sys.stdin.readline

n, c = map(int, input().split())

tmp=[]
for i in range(n):
    x = int(input())
    tmp.append(x)

tmp.sort()
print(tmp)

start = 1 # 최소 거리
end = tmp[-1]-tmp[0] # 최대 거리
cnt=1
result = 0
while start<=end:
    mid = (start + end) // 2 # 중간 간격 거리
    cnt = 1 # 첫번째 원소는 이미 방문한 것으로 침
    curr = tmp[0]

    for i in range(1, len(tmp)):
        if tmp[i] >= mid + curr: # 이동하려는 간격이 (중간간격 거리 + 현재 위치) 보다 크면
            cnt+=1
            curr=tmp[i]
        
    if cnt >= c: # 공유기 설치가 끝났으면, 범위를 좀 더 퍼트려줄 필요가 있다. 
        start=mid+1
        result=mid
    else: # 범위에 못미치면 범위를 줄여줄 필요가 있다. 
        end=mid-1

print(result)



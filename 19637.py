import sys

# 전투력 10,000 이하의 캐릭터는 WEAK
# 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL
# 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호
n, m = map(int, sys.stdin.readline().split())
check=[]
for i in range(n):
    k, value = sys.stdin.readline().split()
    check.append([k, int(value)])
#받은값 정렬해줌 
check = sorted(check, key = lambda x: x[1])

tmp = []
# 값 받고
for i in range(m):
    value = int(sys.stdin.readline().rstrip())
    tmp.append(value)

for i in range(m):
    high = len(check)
    low = 0
    result = 0
    target = tmp[i]
    while low <= high:
        mid = (low + high)//2
        if target <= check[mid][1]:
            high = mid-1
            result = mid
        elif target > check[mid][1]:
            low = mid+1
    print(check[result][0])
        
    
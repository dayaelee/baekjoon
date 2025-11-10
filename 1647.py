n, m = map(int, input().split())
llist = []
for i in range(m):
    llist.append(list(map(int, input().split())))

llist = sorted(llist, key = lambda x: x[2])

# print(llist)

# 특정 원소가 속한 집합 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
            parent[x] = find(parent[x])
            return parent[x]
    return x

# 두 원소가 속한 집합을 합치기
sum = []
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 부모 테이블 초기화 
parent = [0] * (n+1)

# 부모 테이블에서 부모를 자기 자신으로 초기화 
for i in range(1, n+1):
    parent[i]=i

# for i in range(len(llist)):
#     a, b, cost = llist[i]
#     union(a, b)

result=[]

for edge in llist:
    a, b, cost = edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find(a) != find(b): 
        union(a, b)
        result.append(cost)

sum = 0
for i in range(len(result)-1):
    sum+=result[i]
print(sum)
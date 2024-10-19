'''
크기가 N×N인 도시
각 칸은 /빈 칸/치킨집/집
도시의 칸은 (r, c)와 같은 형태
우측하단 ++
r과 c는 1부터 시작

치킨 거리: 집과 가장 가까운 치킨집 사이의 거리

치킨 거리는 집을 기준으로 정해지며
각각의 집은 치킨 거리를 가지고 있다

도시의 치킨 거리: 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는
|r1-r2| + |c1-c2|로 구한

치킨집을 폐업시키려
치킨집의 개수는 최대 M개

도시에 있는 치킨집 중에서 최대 M개를 고르고,
나머지 치킨집은 모두 폐업시켜야 한다. 
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지

'''
import sys
import itertools
input= sys.stdin.readline

n, m = map(int, input().split())
mapp =[]
for i in range(n):
    mapp.append(list(map(int, input().split())))

'''
1. 치킨집 리스트에서 m개의 치킨집을 중복되지 않게 골라서 
2. 각 집에서 모든 치킨집 중 최소거리가 나오는 치킨집을 골라서 
다 더한다. 

1마다 2의 결과를 골라서 젤 작은 값을 출력
'''

chicken =[]
house =[]

for i in range(n):
    for j in range(n):
        if mapp[i][j]==1:
            house.append([i,j])
        elif mapp[i][j]==2:
            chicken.append([i, j])

combi = itertools.combinations(chicken, m)

rresult=1e9

for chic in combi:
    result=0
    for j in house:
        minn=1e9
        for i in chic:
            r1, c1 = j
            r2, c2 = i

            if minn > abs(r1-r2) + abs(c1-c2):
                minn = abs(r1-r2) + abs(c1-c2)
        result+=minn
    if rresult>result:
        rresult=result
print(rresult)

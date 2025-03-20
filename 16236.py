import sys
from collections import deque
n = int(input())
mapp = []
dy=[1, 0, 0, -1]
dx=[0, -1, 1, 0]
me = 2
for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        ci=i
        cj=tmp.index(9)
    mapp.append(tmp)
cnt, ans = 0, 0
mapp[ci][cj]= 0	

def bfs(si, sj):

	q=deque([])
	visited=[[0] * n for _ in range(n)] 
	tlist = []

	q.append((si, sj))
	visited[si][sj]=1
	eat = 0

	while q:
		ci, cj = q.popleft()
		# 꺼내보니 eat == v[ny][nx] 
		if eat == visited[ci][cj]:
			return tlist, eat-1
		
		for i in range(4):
			ny = ci+dy[i]
			nx = cj+dx[i]

			if 0<=ny<n and 0<=nx<n and visited[ny][nx]==0:
				if me >= mapp[ny][nx]:
					visited[ny][nx]=visited[ci][cj]+1
					q.append((ny, nx))
					if me > mapp[ny][nx] > 0:
						tlist.append((ny, nx))
						eat = visited[ny][nx]

	# 방문을 모두 끝낸 경우 
	return tlist, eat-1

while 1:
	tlist, dist = bfs(ci, cj)
	#print(tlist, dist, 'jo')
	if len(tlist) ==0:
		break
	tlist.sort(key=lambda x:(x[0], x[1]))
	ci, cj = tlist[0]
	mapp[ci][cj]=0 # 물고기 먹기 
	cnt+=1
	ans+=dist
	if me == cnt: # 크기만큼 물고기 먹은경우 크기 +1
		me +=1
		cnt = 0

print(ans)         


from collections import deque 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())  # N값 입력

# 높이 정보를 입력받음
tmp = [list(map(int, input().split())) for _ in range(n)]

# BFS 함수 정의
def bfs(x, y, height, visited):
    dq = deque([(x, y)])
    visited[x][y] = True

    while dq:
        px, py = dq.popleft()
        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            # 범위 체크와 방문 여부 확인
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and tmp[nx][ny] > height:
                visited[nx][ny] = True
                dq.append((nx, ny))

# 안전 영역의 최대 개수를 구하기 위한 변수
max_safe_areas = 0
max_height = max(max(row) for row in tmp)  # 지역의 최대 높이

# 높이가 0부터 최대 높이까지 증가하면서 안전 영역을 탐색
for height in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]  # 각 높이마다 방문 기록 초기화
    safe_areas = 0  # 현재 높이에서의 안전 영역 개수

    # 모든 지점에 대해 BFS 실행
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and tmp[i][j] > height:  # 물에 잠기지 않은 지역만 탐색
                safe_areas += 1
                bfs(i, j, height, visited)
                
    # 최대 안전 영역 개수 갱신
    max_safe_areas = max(max_safe_areas, safe_areas)

# 결과 출력
print(max_safe_areas)

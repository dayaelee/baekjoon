'''
N-Queen  N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
퀸은 상하좌우와 대각선 4방향 모두 끝까지 이동할 수있음 
각 퀸의 경로에 다른 퀸이 있어서는 안된다. 
'''
n = int(input())

# 이동용
dy= [1, -1, 0, 1]
dx= [0, 0, -1, 1]

# 말의 공격 범위(상하좌우+대각선)
dyy= [1, -1, 0, 0, 1, 1, -1, -1]
dxx= [0, 0, -1, 1, -1, 1, -1, 1]

mapp = [[0 for _ in range(n)] for _ in range(n)] 

print(mapp)

# 시작을 어디서 부터 하냐에 따라서 갈림 
# 따라서 전체 순회가 필요 
stack = []
visited = [[False for _ in range(n)] for _ in range(n)]
def solution(y, x, visited, cnt):
    for i in range(n):
        for j in range(n):
            stack.append([i, j])
            mapp[i][j]=1
            visited[i][j] = True

            for q in range(8):
                ry = i
                rx = j
                for p in range(n):
                    ry+=dyy[q]
                    rx+=dxx[q]
                    if ry <0 or rx <0 or ry>=n or rx>=n:
                        continue

                    visited[ry][rx]=True

            print('')
            for ii in range(n):
                print('hi',visited[ii])
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
            visited[i][j] = False
            
            for q in range(8):
                ry = i
                rx = j
                for p in range(n):
                    ry+=dyy[q]
                    rx+=dxx[q]
                    if ry <0 or rx <0 or ry>=n or rx>=n:
                        continue

                    visited[ry][rx]=False
            
            print('')
            for ii in range(n):
                print('hi',visited[ii])
            print('???????????????????????????')
            

            stack.pop()

            print(visited)
            mapp[i][j]=0



solution(1, 1, visited, 0)